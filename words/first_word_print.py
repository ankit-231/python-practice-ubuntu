# keep it odd
HEIGHT = 5
WIDTH = 5

WRITER = "▪"
SEPARATOR = " "


def output_W():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # prints the first and last part of W
                (j == 1 or j == w)
                # prints the middle part
                or (i == mh and j == mw)
                # prints the diagonal part
                or (i == mh + 1 and (j == mw - 1 or j == mw + 1))
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_W()


def output_O():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # top and bottom middle lines
                ((i == 1 or i == h) and (j > 1 and j < w))
                # left and right lines
                or ((i > 1 and i < h) and (j == 1 or j == w))
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_O()


def output_R():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # left line
                (j == 1)
                # top and middle line
                or (j < w and (i == 1 or i == mh))
                or (i == 2 and j == h)
                or (i == 4 and j == mw)
                or (i == h and j > mw)
                # first and last dot
                # or ((i > 1 and i < h) and (j == 1 or j == w))
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_R()


def output_D():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # left line
                (j == 1)
                # right line
                or (j == w and (i > 1 and i < h))
                or ((i == 1 or i == h) and j < w)
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_D()


def output_L():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # left line
                (j == 1)
                # bottom line
                or (i == h)
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_L()


def output_E():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            if (
                # left line
                (j == 1)
                # top and bottom line
                or (i == h or i == 1)
                or (i == mh and j < w)
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_E()


def output_all(string: str):
    from words.finals.final_user_input import ACCEPTED_LETTERS

    string = string.upper()
    for i in string:
        if i == "W":
            output_W()
        elif i == "O":
            output_O()
        elif i == "R":
            output_R()
        elif i == "D":
            output_D()
        elif i == "L":
            output_L()
        elif i == "E":
            output_E()
        else:
            raise ValueError(
                f"Word contains letter {i} which is not presented in ACCEPTED_LETTERS: {ACCEPTED_LETTERS}"
            )
