from slugify import slugify
import sys


def get_slug(text):
    return slugify(text)


if __name__ == "__main__":
    # print(get_slug("ankit ///`121``~!!!$#%%^^^&*()-=\/khanal"))
    # print(sys.argv)

    if len(sys.argv) < 2:
        print("Usage: python utilities.py <text>")
    else:
        text = " ".join(sys.argv[1:])
        print(get_slug(text))
