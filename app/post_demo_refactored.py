import os
import requests
from dotenv import load_dotenv
import api_client


load_dotenv()
api_key = os.getenv("MY_API_KEY")


def main():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    try:
        user = api_client.create_user(name, email, api_key)
        print("User created successfully:", user)

    except requests.exceptions.HTTPError:
        print("An HTTP error occurred. Please check the input and try again.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check your internet connection and try again.")



if __name__ == "__main__":
    main()     