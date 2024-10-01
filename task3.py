import requests
from bs4 import BeautifulSoup

# Define the URL of the web application
url = 'http://example.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Identify potential vulnerabilities
vulnerabilities = []

# Check for SQL injection vulnerabilities
if soup.find('input', {'type': 'text'}) and soup.find('form', {'method': 'GET'}):
    vulnerabilities.append('SQL injection vulnerability detected')

# Check for cross-site scripting (XSS) vulnerabilities
if soup.find('script', {'src': 'http://example.com/script.js'}):
    vulnerabilities.append('XSS vulnerability detected')

# Check for cross-site request forgery (CSRF) vulnerabilities
if soup.find('form', {'action': 'http://example.com/action'}) and not soup.find('input', {'name': 'csrf_token'}):
    vulnerabilities.append('CSRF vulnerability detected')

# Print the results
if vulnerabilities:
    print('Vulnerabilities detected:')
    for vuln in vulnerabilities:
        print(vuln)
else:
    print('No vulnerabilities detected')
