import requests


def create_user(name, email):
    new_user = {
        "name": name,
        "email": email
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=new_user,
        timeout=5
    )

    response.raise_for_status()

    return response.json()



def display_created_user(user):
    print("User created successfully!")
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])


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
        created_user = create_user(name, email)

        display_created_user(created_user)


    except requests.exceptions.HTTPError:
        print("Something went wrong while contacting the server. Please try again later.")


    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")


    except requests.exceptions.ConnectionError:
        print("There was a connection error. Please check your internet connection and try again.")



if __name__ == "__main__":
    main()        