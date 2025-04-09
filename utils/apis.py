import requests
import random
import string


class APIS:
    base_url = "https://gorest.co.in/"


    def __init__(self):
        self.header = {
            "Authorization" : "Bearer 77623844a42b24e0f48a62055ebbd789068b57ef4643a6063b3253df5ea8d5c5",
            "Content-Type":"application/json"
        }

    def get(self,endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url,headers=self.header)
        return response

    def post(self,endpoint,body):
        url = f'{self.base_url}/{endpoint}'
        response = requests.post(url,headers=self.header,json=body)
        return response

    def put(self,endpoint,body):
        url = f'{self.base_url}/{endpoint}'
        response = requests.put(url, headers=self.header, json=body)
        return response

    def delete(self,endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.delete(url, headers=self.header)
        return response


    def generate_email(self):
        domain = "gmail.com"
        email_length = 10
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
        email_id = random_string + "@" + domain
        return email_id