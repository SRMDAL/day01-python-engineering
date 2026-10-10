import logging
import requests
from app import api_client


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def main():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    try:
        logging.info("Starting user creation request.")

        user = api_client.create_user(name, email)
        print("User created successfully:")
        print(user)

    except requests.exceptions.HTTPError:
        logging.exception("User creation request failed with an HTTP error.")
        print("The server rejected the request. Please try again.")


    except requests.exceptions.Timeout:
        logging.exception("User creation request timed out.")
        print("Request timed out. Please try again later.")

        
    except requests.exceptions.ConnectionError:
        logging.exception("User creation request failed due to a connection error.")
        print("Connection error. Please check your internet connection.")



if __name__ == "__main__":
    main()