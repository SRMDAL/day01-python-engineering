import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise ValueError("MY_API_KEY is not set.")


def get_headers(api_key: str) -> dict:
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return headers




def get_user(user_id: int) -> dict:
    # create headers
    headers = get_headers(api_key)
    
    # build URL here
    url= f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # send GET request here
    response = requests.get(
        url,
        headers=headers,
        timeout=5
    )

    # check response here
    response.raise_for_status()

    # return JSON here
    return response.json()



def create_user(name: str, email: str) -> dict:
    headers = get_headers(api_key)

    new_user = {
        "name": name,
        "email": email
    }

    response = requests.post(
        'https://jsonplaceholder.typicode.com/users',
        headers=headers,
        json=new_user,
        timeout=5
    )

    response.raise_for_status()

    return response.json()