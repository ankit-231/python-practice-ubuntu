# keep it odd
HEIGHT = 5
WIDTH = 5

WRITER = "*"
SEPARATOR = " "
LETTER_SEPARATOR = ""


def condition_for_letter(letter: str, row: int, column: int):
    left_index = 0
    right_index = WIDTH - 1
    top_index = 0
    bottom_index = HEIGHT - 1
    middle_height_index = WIDTH // 2
    middle_width_index = HEIGHT // 2
    if letter == "W":
        return (
            # prints the first and last part of W
            (column == left_index or column == right_index)
            # prints the middle part
            or (row == middle_height_index and column == middle_width_index)
            # prints the diagonal part
            or (
                row == middle_height_index + 1
                and (
                    column == middle_width_index - 1 or column == middle_width_index + 1
                )
            )
        )
    elif letter == "O":

        return (
            # top and bottom middle lines
            (
                (row == top_index or row == bottom_index)
                and (column > left_index and column < right_index)
            )
            # left and right lines
            or (
                (row > top_index and row < bottom_index)
                and (column == left_index or column == right_index)
            )
        )
    elif letter == "R":
        return (  # left line
            (column == left_index)
            # top and middle line
            or (
                column < right_index
                and (row == top_index or row == middle_height_index)
            )
            or (row == 1 and column == right_index)
            or (row == 3 and column == middle_width_index)
            or (row == bottom_index and column > middle_width_index)
        )
    elif letter == "D":
        return (
            # left line
            (column == left_index)
            # right line
            or (column == right_index and (row > top_index and row < bottom_index))
            or ((row == top_index or row == bottom_index) and column < right_index)
        )
    elif letter == "L":
        return (
            # left line
            (column == left_index)
            # bottom line
            or (row == bottom_index)
        )
    elif letter == "E":
        return (
            # left line
            (column == left_index)
            # top and bottom line
            or (row == bottom_index or row == top_index)
            or (row == middle_height_index and column < right_index)
        )
    else:
        raise ValueError("Not W,O")


def get_main_list():
    main_li = [[SEPARATOR] * WIDTH for h in range(HEIGHT)]
    return main_li


def output_W_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("W", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_O_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("O", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_R_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("R", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_D_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("D", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_L_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("L", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_E_list():
    main_li = get_main_list()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if condition_for_letter("E", i, j):
                main_li[i][j] = WRITER
    return main_li


def output_all(string: str):
    all_list = []

    from final_user_input import ACCEPTED_LETTERS

    string = string.upper()

    for i in string:
        if i == "W":
            all_list.append(output_W_list())
        elif i == "O":
            all_list.append(output_O_list())
        elif i == "R":
            all_list.append(output_R_list())
        elif i == "D":
            all_list.append(output_D_list())
        elif i == "L":
            all_list.append(output_L_list())
        elif i == "E":
            all_list.append(output_E_list())
        else:
            raise ValueError(
                f"Word contains letter {i} which is not presented in ACCEPTED_LETTERS: {ACCEPTED_LETTERS}"
            )

    for i in range(len(all_list[0])):
        for j in range(len(all_list)):
            print("".join(all_list[j][i]), end=LETTER_SEPARATOR)
        print()
