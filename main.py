import os

DIRECTORY = r''#путь к папке


def files(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            rename(root, name)