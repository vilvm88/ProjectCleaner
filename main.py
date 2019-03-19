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
    r"\Deployment",
    r"\Coverage",
    ".axoCover"
]

excludes = [
    r".git",
    "Release_1_0",
    "ADM_1824"
]


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    return parser.parse_args()


def append(list, path):
    if not path in list:
        list.append(path)


def remove(list, path):
    if path in list:
        list.remove(path)


def get_directories_for_clean(path):
    directories = []

    for dirname, dirnames, filenames in os.walk(path):
        if not os.listdir(dirname):
            append(directories, dirname)

        for dir in includes:
            if dirname.endswith(dir):
                append(directories, dirname)
                break

        for dir in excludes:
            if dir in dirnames:
                remove(directories, dirname)
                break

            if dirname.find(dir) >= 0:
                remove(directories, dirname)
                break

    return directories


def clean(path):
    directories = get_directories_for_clean(path)

    if len(directories) == 0:
        return 0

    for dir in directories:
        if not os.path.isdir(dir):
            continue
        shutil.rmtree(dir)
        print(dir, "removed")

    return len(directories)


def main():
    args = get_arguments()

    while True:
        if clean(args.directory) == 0:
            break


if __name__ == "__main__":
    main()
