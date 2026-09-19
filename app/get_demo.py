import requests

import api_client 





def main():
    user_id = input("Enter user ID: ").strip()


   
    try:
        # convert user_id to an integer here
        user_id = int(user_id)

        if user_id <= 0:
            print("User ID must be greater than 0.")
            return

    except ValueError:
        # print a friendly error message here
        print("Invalid user ID. Please enter a valid integer.")
        return



    # call get_user()
    try:
        user = api_client.get_user(user_id)
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