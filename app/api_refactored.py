import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise ValueError("MY_API_KEY is not set.")

headers = {"Authorization": f"Bearer {api_key}"}



def get_user(user_id):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={"id": user_id},
        headers=headers,
        timeout=5
        
    )
    
    response.raise_for_status()
    users = response.json()

    return users    


def display_user(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print(f"Company: {user['company']['name']}")



def main():
    user_id = input("Enter user ID: ")


    if not user_id.isdigit():
        print("Please enter a valid number.")
        return


    try:
        users = get_user(user_id)


        if users:
            display_user(users[0])

        else:
            print("User not found.")


    except requests.exceptions.HTTPError:
        print("Something went wrong while contacting the server. Please try again later.")    

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("There was a connection error. Please check your internet connection and try again.")




if __name__ == "__main__":
    main()

   
