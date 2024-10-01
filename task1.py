import socket

# Define the target IP address and port range
target_ip = '192.168.1.132'
start_port = 1
end_port = 32

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Scan the network for open ports and services
for port in range(start_port, end_port + 1):
    try:
        # Attempt to connect to the target IP address and port
        sock.connect((target_ip, port))
        print(f"Port {port} is open")
    except socket.error:
        print(f"Port {port} is closed")
    finally:
        # Close the socket connection
        sock.close()

# Identify and document potential vulnerabilities
vulnerabilities = []

for port in range(start_port, end_port + 1):
    try:
        # Attempt to connect to the target IP address and port
        sock.connect((target_ip, port))
        # Check for common vulnerabilities
        if port == 22:
            vulnerabilities.append('SSH service detected on port 22')
        elif port == 80:
            vulnerabilities.append('HTTP service detected on port 80')
        elif port == 443:
            vulnerabilities.append('HTTPS service detected on port 443')
    except socket.error:
        pass
    finally:
        # Close the socket connection
        sock.close()

# Print the vulnerabilities
if vulnerabilities:
    print('Potential vulnerabilities detected:')
    for vuln in vulnerabilities:
        print(vuln)
else:
    print('No potential vulnerabilities detected')
