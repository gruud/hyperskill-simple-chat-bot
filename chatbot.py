"""Hyperskill Simple Chat Bot implementation - Step 4"""

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

    count = int(input("Now I will prove to you that I can count to any number you want.\n"))
    for number in range(0, count+1):
        print(f"{number} !")
    print("Completed, have a nice day!")


if __name__ == "__main__":
    main()