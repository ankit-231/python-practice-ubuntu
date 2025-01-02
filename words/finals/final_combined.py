from final_user_input import get_user_input, ACCEPTED_LETTERS, BREAK_WORD
from outputlist import output_all


def main():
    while True:
        user_input = get_user_input()
        if user_input == BREAK_WORD:
            print("Thank you for using our application!")
            break

        output_all(user_input)


main()
