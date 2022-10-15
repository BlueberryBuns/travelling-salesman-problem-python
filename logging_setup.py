import logging


def logging_setup():
    logging.basicConfig(
        format="[%(asctime)s]: %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        level=logging.INFO,
    )
