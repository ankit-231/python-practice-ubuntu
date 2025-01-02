ACCEPTED_LETTERS = ["W", "O", "R", "D", "L", "E"]
BREAK_WORD = "END"


def get_user_input():
    while True:
        user_input = input("Enter a word: ")

        # case sensitive break word
        if user_input == BREAK_WORD:
            return user_input

        # check if input string is empty
        if user_input == "":
            print(
                "Please enter valid word containing only W, O, R, D, L and/or E or the break word END"
            )
            continue

        # case insensitive words
        user_input = user_input.upper()

        for letter in user_input:
            if letter not in ACCEPTED_LETTERS:
                print(
                    "Please enter valid word containing only W, O, R, D, L and/or E or the break word END"
                )
                break

        else:
            print("Word accepted")
            return user_input


# user_input = get_user_input()

# print(user_input)

# if user_input == BREAK_WORD:
#     print("Thank you!")
