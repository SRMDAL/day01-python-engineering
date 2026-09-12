import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise ValueError("MY_API_KEY is not set.")


def get_headers(api_key):
    headers = {'Authorization': f'Bearer {api_key}'}  
    return  headers  


def get_user(user_id, headers):
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






def main():
    user_id = input("Enter user ID: ").strip()

    try:
        # convert user_id to an integer here
        user_id = int(user_id)

    except ValueError:
        # print a friendly error message here
        print("Invalid user ID. Please enter a valid integer.")
        return


    # create headers
    headers = get_headers(api_key)


    # call get_user()
    try:
        user = get_user(user_id, headers)
        # print the result
        print(user)
    
    except requests.exceptions.HTTPError:
        # print a friendly message
        print("User could not be found. Please check the user ID and try again.")

    except requests.exceptions.Timeout:
        # friendly timeout message
        print("Request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        # friendly connection error message
        print("Connection error occurred. Please check your internet connection and try again.")





if __name__ == "__main__":
    main()    