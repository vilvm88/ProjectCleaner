import glob
import os
import shutil
import argparse

includes = [
    r"\TestsBin",
    r"\obj",
    r"\bin",
    r"\Bin",
    r"\Debug",
    r"\Relese",
    r"\Deployment"
]

excludes = [
    r".git",
    r"\Deployment\Release_1_0",
    r"\Deployment\ADM_1824"
]


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    return parser.parse_args()


def get_directories_for_clean(path):
    directories = []

    for dirname, dirnames, filenames in os.walk(path):
        if not os.listdir(dirname):
            directories.append(dirname)
            continue

        for dir in excludes:
            if dirname.find(dir) >= 0 and dir in directories:
                directories.remove(dir)
                break

        for dir in includes:
            if dirname.endswith(dir):
                directories.append(dirname)

    return directories


def clean(path):

    directories = get_directories_for_clean(path)

    if len(directories) == 0:
        return 0

    count = 0
    for dir in directories:
        if not os.path.isdir(dir):
            continue
        shutil.rmtree(dir)
        print(dir, "removed")
        count += 1
    return count


def main():
    args = get_arguments()

    while True:
        if clean(args.directory) == 0:
            break


if __name__ == "__main__":
    main()
