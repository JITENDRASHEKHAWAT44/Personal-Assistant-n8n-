import requests 

user_message = "can you become job ready in 3 months as cse student?"

request_message = {"message" : user_message}

url = "https://buildern8n.app.n8n.cloud/webhook-test/8bf5c086-0e5c-43b4-acd5-c0b5a2d889cf"

response = requests.post(url , json = request_message)

print(response.status_code)
print(response.json()[0]["output"])