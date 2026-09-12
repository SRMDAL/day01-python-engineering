import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise ValueError("MY_API_KEY is not set.")
 



def get_headers(api_key):
    # create headers dictionary
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    # return headers
    return headers



def create_user(name, email, headers):
    # build new_user here
    new_user = {
        "name": name,
        "email": email
    }

    # send POST request here
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        headers=headers,
        json=new_user,
        timeout=5
    )
    # check the response here
    response.raise_for_status()

    # return the JSON here
    return response.json()



def main():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty. Please enter a valid name.")
        return

    email = input("Enter email: ").strip()

    if not email:
        print("Email cannot be empty. Please enter a valid email.")
        return


    try:
        headers = get_headers(api_key)
        created_user = create_user(name, email, headers)

        print(created_user)

    except requests.exceptions.HTTPError:
        print("Something went wrong while contacting the server. Please try again later.")

    except requests.exceptions.Timeout:

        print("The request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("There was a connection error. Please check your internet connection and try again.")






if __name__ == "__main__":
    main()