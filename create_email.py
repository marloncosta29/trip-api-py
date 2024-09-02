import requests

payload = {
    "requestor": "dback_trip",
    "version": "1.0"
}
response = requests.post('https://api.nodemailer.com/user', json=payload)
if response.status_code == 200:
    account = response.json()
    print(account)
else:
    raise Exception(f'could not create a Ethereal account: {response.text}')