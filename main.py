import glob
import os
import shutil
import argparse

directories = [
    "TestsBin",
    "obj",
    "bin",
    "Debug",
    "Relese"
]


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    return parser.parse_args()


def main():
    args = get_arguments()

    for dirname, dirnames, filenames in os.walk(args.directory):
        for dir in directories:
            if dirname.endswith(dir):
                shutil.rmtree(dirname)
                print(dirname, "removed")


if __name__ == "__main__":
    main()
