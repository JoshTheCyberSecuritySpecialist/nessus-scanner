import requests
import json

# API Credentials
access_key = "your_access_key_here"
secret_key = "your_secret_key_here"
base_url = "https://<your-nessus-server-ip>:8834"

# Headers for Authentication
headers = {
    "X-ApiKeys": f"accessKey={access_key}; secretKey={secret_key}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def list_scans():
    """Fetch a list of all available scans."""
    url = f"{base_url}/scans"
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        scans = response.json()['scans']
        print("Available Scans:")
        for scan in scans:
            print(f"- {scan['name']} (ID: {scan['id']})")
    else:
        print(f"Failed to list scans: {response.status_code}")

def launch_scan(scan_id):
    """Launch a specific scan by ID."""
    url = f"{base_url}/scans/{scan_id}/launch"
    response = requests.post(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        print(f"Successfully launched scan ID: {scan_id}")
    else:
        print(f"Failed to launch scan: {response.status_code}")

def get_scan_results(scan_id):
    """Retrieve the results of a scan."""
    url = f"{base_url}/scans/{scan_id}"
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        scan_data = response.json()
        print(json.dumps(scan_data, indent=2))
    else:
        print(f"Failed to retrieve scan results: {response.status_code}")

if __name__ == "__main__":
    # List all scans
    list_scans()
    
    # Example: Launch a scan by ID (replace with a valid ID)
    scan_id = input("Enter the scan ID to launch: ")
    launch_scan(scan_id)

    # Fetch the scan results
    input("Press Enter after scan completes to view results...")
    get_scan_results(scan_id)
