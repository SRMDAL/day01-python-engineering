import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_API_KEY")
print(api_key is not None)
headers = {"Authorization": f"Bearer {api_key}"}
print(headers)

user_id = input("Enter user ID: ")

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={"id": user_id},
        headers=headers,
        timeout=5
        
    )


    response.raise_for_status()

    users = response.json()

    if users:
        print(f"Name: {users[0]['name']}")
        print(f"Email: {users[0]['email']}")
        print(f"City: {users[0]['address']['city']}")
        print(f"Company: {users[0]['company']['name']}")
    else:
        print("User not found.")


except requests.exceptions.HTTPError:
    print("Something went wrong with the API request.")

except requests.exceptions.Timeout:
    print("The API request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API.")



   
