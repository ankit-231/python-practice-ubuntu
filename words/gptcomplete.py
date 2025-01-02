# def print_W():
#     return [
#         "*     *",
#         "*     *",
#         "*  *  *",
#         "* * * *",
#         "*     *"
#     ]

# def print_O():
#     return [
#         "*****",
#         "*   *",
#         "*   *",
#         "*   *",
#         "*****"
#     ]

# def print_R():
#     return [
#         "*****",
#         "*   *",
#         "*****",
#         "*  *",
#         "*   *"
#     ]

# def print_D():
#     return [
#         "****",
#         "*   *",
#         "*   *",
#         "*   *",
#         "****"
#     ]

# def print_L():
#     return [
#         "*",
#         "*",
#         "*",
#         "*",
#         "*****"
#     ]

# def print_E():
#     return [
#         "*****",
#         "*",
#         "*****",
#         "*",
#         "*****"
#     ]

# def print_word(word):
#     letter_funcs = {
#         'W': print_W,
#         'O': print_O,
#         'R': print_R,
#         'D': print_D,
#         'L': print_L,
#         'E': print_E
#     }

#     grid = [""] * 5  # Initialize a list with 5 empty strings for 5 rows

#     for letter in word.upper():
#         letter_grid = letter_funcs[letter]()
#         for i in range(5):
#             grid[i] += letter_grid[i] + " "  # Concatenate each row

#     for row in grid:
#         print(row)

# def is_valid_word(word):
#     valid_letters = set("WORDLE")
#     return all(char in valid_letters for char in word.upper())

# def main():
#     while True:
#         user_input = input("Enter a word (or 'END' to stop): ")
#         if user_input == "END":
#             break
#         elif is_valid_word(user_input):
#             print_word(user_input)
#         else:
#             print("Invalid input. Please enter a word using only the letters W, O, R, D, L, E.")

# if __name__ == "__main__":
#     main()


HEIGHT = 5
WIDTH = 5

WRITER = "▪"
SEPARATOR = " "
SPACE_BETWEEN = 0


def print_side_by_side(shape_conditions1, shape_conditions2):
    height_plus_one = HEIGHT + 1
    width_plus_space = WIDTH * 2 + SPACE_BETWEEN + 1

    for i in range(1, height_plus_one):
        for j in range(1, width_plus_space):
            if j <= WIDTH:
                # Conditions for the first letter (W)
                if shape_conditions1(i, j):
                    print(WRITER, end="")
                else:
                    print(SEPARATOR, end="")
            elif j > WIDTH + SPACE_BETWEEN:
                # Adjust j for the second letter (O)
                adj_j = j - WIDTH - SPACE_BETWEEN
                if shape_conditions2(i, adj_j):
                    print(WRITER, end="")
                else:
                    print(SEPARATOR, end="")
            else:
                # Space between letters
                print(SEPARATOR, end="")
        print()


def output_WO():
    mid_height = HEIGHT // 2 + 1
    mid_width = WIDTH // 2 + 1

    def shape_conditions_W(i, j):
        return (
            j == 1
            or j == WIDTH
            or (i == mid_height and j == mid_width)
            or (i == mid_height + 1 and (j == mid_width - 1 or j == mid_width + 1))
        )

    def shape_conditions_O(i, j):
        return ((i == 1 or i == HEIGHT) and (j > 1 and j < WIDTH)) or (
            (i > 1 and i < HEIGHT) and (j == 1 or j == WIDTH)
        )

    print_side_by_side(shape_conditions_W, shape_conditions_O)


# Call the function to print W and O side by side
output_WO()
