# keep it odd
HEIGHT = 5
WIDTH = 5
OWIDTH = 5

WRITER = "▪"
SEPARATOR = " "


def mw():
    return WIDTH // 2


def mh():
    return HEIGHT // 2


def condition_for_letter(letter: str, i: int, j: int):
    if letter == "W":
        return (
            # prints the first and last part of W
            (j == 0 or j == WIDTH - 1)
            # prints the middle part
            or (i == mh() and j == mw())
            # prints the diagonal part
            or (i == mh() + 1 and (j == mw() - 1 or j == mw() + 1))
        )
    elif letter == "O":

        return (
            # top and bottom middle lines
            ((i == 1 or i == HEIGHT) and (j > 1 and j < WIDTH))
            # left and right lines
            or ((i > 1 and i < HEIGHT) and (j == 1 or j == WIDTH))
        )

    else:
        raise ValueError("Not W,O")


main_li = [[SEPARATOR] * 5 * 2 for _ in range(HEIGHT)]

# [[SEPARATOR] * WIDTH] * HEIGHT


def output_W():
    text = "WO"
    for letter in text:
        for i in range(0, HEIGHT):
            for j in range(0, WIDTH):
                if letter == "W":
                    if condition_for_letter("W", i, j):
                        # print(f"({i},{j})", end="")
                        main_li[i][j] = WRITER
                        # print(WRITER, end="")
                else:
                    if condition_for_letter("O", i, j):
                        adjusted_j = j + WIDTH
                        # print(adjusted_j, "Dsadsa")
                        main_li[i][adjusted_j] = WRITER
            # print()
        # print(main_li)
    for row in main_li:
        print("".join(row))
        # print(row)


output_W()

# output_W()


# def output_WO():
#     height_plus_1 = HEIGHT + 1
#     width_plus_1 = WIDTH + 1
#     main_list = []
#     for i in range(1, height_plus_1):
#         temp_list = []
#         temp_str = ""
#         for j in range(1, width_plus_1):
#             for k in range(5):
#                 if condition_for_letter("W", i, j):
#                     print(WRITER, end="")
#                     temp_list.append(WRITER)
#                     temp_str += WRITER
#                 else:
#                     print(SEPARATOR, end="")
#                     temp_list.append(SEPARATOR)
#                     temp_str += SEPARATOR

#             for l in range(5):
#                 if condition_for_letter("O", i, j):
#                     print("o", end="")
#                     temp_list.append("o")
#                     temp_str += "o"

#                 else:
#                     print("-", end="")
#                     temp_list.append("-")
#                     temp_str += "-"

#         # main_list.append(temp_list)
#         main_list.append(temp_str)
#         print()
#     print("main_list")
#     for f in main_list:
#         print(f)
#     # print(main_list)


# output_WO()
