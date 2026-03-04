import requests

base_url = 'https://yougile.com/api-v2'
email = ''
password = ''
company_id = ''


def get_token(email, password, company_id):
    body = {
        "login": email,
        "password": password,
        "companyId": company_id
    }
    resp = requests.post(base_url + '/auth/keys', json=body)
    return resp.json()


result = get_token(email, password, company_id)
token = result.get("key")
print(token)
