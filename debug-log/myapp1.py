import logging
import os

# Get the absolute path of the current file
current_file = os.path.abspath(__file__)

logger = logging.getLogger("myapp")


def do_something():
    print("Doing something")


def main():
    # Customize the log format
    logging.basicConfig(
        filename="myapp.log",
        level=logging.DEBUG,
        format=f"%(asctime)s - %(name)s - %(levelname)s - {current_file}:%(lineno)d - %(message)s",
    )
    logger.info("Started")
    do_something()
    logger.debug("Finished")


if __name__ == "__main__":
    main()
