import os
from sys import *


def Check_content(path):
    print("The path is::", path)
    cobj=open(argv[1],'r')
    copy_content=cobj.read()
    print("Copy Content",copy_content)
    fobj = open(argv[2], 'r')
    f_content=fobj.read()

    if copy_content == f_content :
        print("Success")
    else:
        print("Failure")


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of argumnets")
    try:
        Check_content(argv[1])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()