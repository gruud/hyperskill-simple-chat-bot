"""Hyperskill Simple Chat Bot implementation - Step 5"""


def handle_presentation():
    bot_name = "Bacchus"
    birth_year = 2023

    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def handle_username():
    user_name = input("Please, remind me your name.\n")
    print(f"What a great name you have, {user_name}!")


def handle_user_age():
    print("Let me guess your age.")
    remainder3 = int(input("Enter remainders of dividing your age by 3, 5 and 7."))
    remainder5 = int(input())
    remainder7 = int(input())
    age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
    print(f"\nYour age is {age}; that's a good time to start programming!")


def handle_counting():
    count = int(input("Now I will prove to you that I can count to any number you want.\n"))
    for number in range(0, count + 1):
        print(f"{number} !")


def handle_quizz():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    correct_answer = 2
    message = "\n"
    while True:
        answer = int(input(message))
        if answer == correct_answer:
            break
        else:
            message = "Please, try again.\n"



def main():
    """ Main program."""

    handle_presentation()
    handle_username()
    handle_user_age()
    handle_counting()
    handle_quizz()

    print("Congratulations, have a nice day!")


if __name__ == "__main__":
    main()
