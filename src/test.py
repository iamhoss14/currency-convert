import requests

url = "https://v6.exchangerate-api.com/v6/285dfe149039c038fec336df/latest/USD"

response = requests.get(url, timeout=20)

if response.status_code != 200:
    raise RuntimeError(f"Request failed with status {response.status_code}: {response.text[:200]}")

content_type = response.headers.get("Content-Type", "")
if "application/json" not in content_type.lower():
    raise ValueError(f"The API did not return JSON. Content-Type: {content_type}. Response: {response.text[:200]}")

try:
    data = response.json()
except ValueError as exc:
    raise ValueError(f"Invalid JSON received from the API: {response.text[:200]}") from exc

print(data)
