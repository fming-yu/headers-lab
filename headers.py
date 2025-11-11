"""
headers.py
CSC 323 Lab Automation Part 1
Author: Professor Ming
"""

import requests
import json

def main():
    # Custom message
    print("Running headers.py - GitHub Actions Lab Demo")

    # Example request to a stable domain
    url = "https://example.com"
    response = requests.get(url)

    # Print status
    print(f"Request to {url} returned status code {response.status_code}")

    # Save headers to output.json
    headers = dict(response.headers)
    with open("output.json", "w") as f:
        json.dump(headers, f, indent=4)

    print("Response headers saved to output.json")

if __name__ == "__main__":
    main()
