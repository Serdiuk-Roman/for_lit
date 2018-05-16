"""

    read file

"""

from os import path
# import logging


with open('tenor.gif', 'rb') as f:
    print(f.read(10))
    print(path.abspath('smiley_PNG189.png'))
    # f.seek(0)

# add filemode="w" to overwrite
# logging.basicConfig(filename="myapp.log", level=logging.INFO)

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")
# DEBUG, INFO, WARNING, ERROR и CRITICAL

# my_log = logging.getLogger()

# bash pickle

# import logging
# import mylib

# logging.StreamHandler()
# https://habr.com/post/342734/
# генерация json армии
