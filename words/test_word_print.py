# keep it odd
HEIGHT = 21
WIDTH = 21

# WRITER = " ▪ "
# SEPARATOR = " "
WRITER = "|"
SEPARATOR = "."


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
                or ((i > mh and i < h) and (j == mw - 1 or j == mw + 1))
            ):
                print(WRITER, end="")
            else:
                print(SEPARATOR, end="")
        print()


# output_W()


def output_O():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1
    radius = WIDTH // 2
    center_x, center_y = 1 + radius, 1 + radius
    # h = HEIGHT
    # w = WIDTH
    # mh = h // 2 + 1
    # mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            # if (
            #     # prints the first and last part of W
            #     (j == 1 or j == w)
            #     # prints the middle part
            #     or (i == mh and j == mw)
            #     # prints the diagonal part
            #     or ((i > mh and i < h) and (j == mw - 1 or j == mw + 1))
            # ):

            if ((i - center_x) ** 2 + (j - center_y) ** 2) == radius**2:
                print(WRITER, end="")
                # print(f"({i},{j})", end="")
            else:
                print(SEPARATOR, end="")
                # print(f"({i},{j})", end="")
        print()


output_O()

def output_grid():
    h_ = HEIGHT + 1
    w_ = WIDTH + 1

    h = HEIGHT
    w = WIDTH
    mh = h // 2 + 1
    mw = w // 2 + 1
    for i in range(1, h_):
        for j in range(1, w_):
            print(WRITER, end="")
        print()

# output_grid()