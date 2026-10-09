from app import api_client
import requests


def main():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    try:
        user = api_client.create_user(name, email)
        print("User created successfully:")
        print(user)

    except requests.exceptions.HTTPError:
        print("The server rejected the request. Please try again.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")



if __name__ == "__main__":
    main()