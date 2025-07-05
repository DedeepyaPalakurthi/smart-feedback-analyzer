import requests

url = "http://127.0.0.1:8080/predict"
payload = {"text": "I really enjoyed the service. Great job!"}

response = requests.post(url, json=payload)

print("Response:", response.json())
