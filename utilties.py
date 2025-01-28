from slugify import slugify
import sys
import os

available_operations = ["slugify", "slugpy", "hackpy"]


def get_slug(text):
    return slugify(text, separator="_")


def create_file(directory: str, filename: str):
    full_path = os.path.join(directory, filename)
    f = open(full_path, "w")
    f.close()


def print_help():
    print("Usage: python utilities.py --<operation> <text>")
    print("Usage slugify: python utilities.py --slugify <text>")
    print("Usage slugpy: python utilities.py --slugpy <text>")
    print("Usage hackpy: python utilities.py --hackpy <text>")
    print(f"Available Operations: {available_operations}")


if __name__ == "__main__":
    # print(get_slug("ankit ///`121``~!!!$#%%^^^&*()-=\/khanal"))
    # print(sys.argv)
    if len(sys.argv) < 2:
        # print("Usage: python utilities.py <text>")
        print_help()

    else:
        operation_str = sys.argv[1]
        if not "--" in operation_str:
            print_help()
        else:
            actual_operation = operation_str.split("--")[1]
            if actual_operation not in available_operations:
                print_help()

            if (
                actual_operation == "slugify"
                or actual_operation == "slugpy"
                or actual_operation == "hackpy"
            ):
                text = " ".join(sys.argv[2:])
                slug = get_slug(text)
                if actual_operation == "slugpy":
                    slug = slug + ".py"

                if actual_operation == "hackpy":
                    directory = "hackerrank"
                    create_file(directory, slug)
                    print(f"Created {slug} in {directory}.")
                print(slug)
