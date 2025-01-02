# myapp.py
import logging

logger = logging.getLogger("myapp: ")


def do_something():
    print("Doing something")


def main():
    logging.basicConfig(filename="myapp.log", level=logging.DEBUG)
    logger.info("Started")
    do_something()
    logger.debug("Finished")


if __name__ == "__main__":
    main()
