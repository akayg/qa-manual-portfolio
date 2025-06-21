import requests  # Import the requests library to make HTTP requests

# Define the URL for the API endpoint
url = "https://reqres.in/api/login"

# Define the headers for the HTTP request
headers = {
    "x-api-key": "reqres-free-v1",  # Example API key for authentication (not required for this API)
    "Content-Type": "application/json"  # Specify the content type as JSON
}

# Define the payload (data) for the POST request
data = {
    "email": "eve.holt@reqres.in",  # Email address for login
    "password": "cityslica"         # Password for login
}

# Make a POST request to the API endpoint with the specified data and headers
response = requests.post(url, json=data, headers=headers)

# Print the status code of the response (e.g., 200 for success)
print("Status code", response.status_code)

# Print the JSON response returned by the API
print("JSON response", response.json())