import subprocess
import requests
import time
import json

# Nessus server details
NESSUS_URL = 'https://localhost:8834'  # Nessus Web interface
NESSUS_ACCESS_KEY = 'your_access_key'
NESSUS_SECRET_KEY = 'your_secret_key'

# Disable SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Function to run Nmap scan
def run_nmap_scan(target_ip):
    """Run an Nmap scan to discover open ports and services."""
    command = f"nmap -sS -sV -O --script=vuln {target_ip} -oX nmap_results.xml"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Nmap scan completed for {target_ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap scan: {e}")

# Function to create and start a Nessus scan
def create_nessus_scan(target_ip):
    """Create a new scan in Nessus."""
    url = f"{NESSUS_URL}/session"
    auth_data = {
        "username": "your_username",  # Replace with your Nessus username
        "password": "your_password"   # Replace with your Nessus password
    }

    try:
        # Start a session with Nessus
        print("Attempting to connect to Nessus...")
        session = requests.post(url, json=auth_data, verify=False)
        session.raise_for_status()  # Will raise an HTTPError for bad responses (4xx or 5xx)
        session_data = session.json()

        if 'token' in session_data:
            token = session_data['token']
            print(f"Authenticated with Nessus. Token: {token}")

            # Define scan parameters
            scan_data = {
                "uuid": "your_scan_template_uuid",  # Replace with actual scan template UUID
                "settings": {
                    "name": f"Vulnerability Scan for {target_ip}",
                    "text_targets": target_ip
                }
            }

            # Start the scan
            scan_url = f"{NESSUS_URL}/scans"
            scan_response = requests.post(scan_url, headers={'X-Cookie': f'token={token}'}, json=scan_data, verify=False)
            scan_response.raise_for_status()
            scan_id = scan_response.json()['scan']['id']
            print(f"Scan started with ID: {scan_id}")
            return scan_id
        else:
            print("Authentication failed.")
            return None
    except requests.exceptions.ConnectionError as ce:
        print(f"Connection Error: {ce}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting Nessus API: {e}")
    return None

if __name__ == "__main__":
    target_ip = input("Enter target IP address for scanning: ")
    run_nmap_scan(target_ip)

    scan_id = create_nessus_scan(target_ip)
    if scan_id:
        print(f"Scan ID: {scan_id}")
    else:
        print("Failed to start the Nessus scan.")
