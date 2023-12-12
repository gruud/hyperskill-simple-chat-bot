"""Hyperskill Simple Chat Bot implementation - Step 3"""

def main():
    """ Main program."""
    bot_name = "Bacchus"
    birth_year = 2023

    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

    user_name = input("Please, remind me your name.\n")
    print(f"What a great name you have, {user_name}!")

    print("Let me guess your age.")
    remainder3 = int(input("Enter remainders of dividing your age by 3, 5 and 7."))
    remainder5 = int(input())
    remainder7 = int(input())
    age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
    print(f"\nYour age is {age}; that's a good time to start programming!")


if __name__ == "__main__":
    main()