import requests
import api_client





def main():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    try:
        user = api_client.create_user(name, email)
        print("User created successfully:", user)

    except requests.exceptions.HTTPError:
        print("An HTTP error occurred. Please check the input and try again.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check your internet connection and try again.")



if __name__ == "__main__":
    main()     