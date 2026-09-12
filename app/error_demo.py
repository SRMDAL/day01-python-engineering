def main():
    try:
        number = int(input("Enter a number: "))
        print(f"You entered {number}.")
    except ValueError:
        print("That was not a valid number.")


if __name__ == "__main__":
    main()