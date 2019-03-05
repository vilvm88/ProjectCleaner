import glob
import os
import shutil
import argparse

directories = [
    r"\TestsBin",
    r"\obj",
    r"\bin",
    r"\Bin",
    r"\Debug",
    r"\Relese",
    r"\Deployment"
]


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    return parser.parse_args()


def main():
    args = get_arguments()

    for dirname, dirnames, filenames in os.walk(args.directory):
        for dir in directories:
            if dirname.endswith(dir) and dirname.find(".git") == -1:
                shutil.rmtree(dirname)
                print(dirname, "removed")


if __name__ == "__main__":
    main()
