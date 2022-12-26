from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    return  hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, filList in os.walk(path):
            for filen in filList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    result = list(filter(lambda x: len(x) > 1,dict1.values()))

    if len(result) > 0:
        print("Duplicates Found:")

        print("The following files are identical.")

        icnt = 0;
        for result in result:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    print('\t\t%s' % subresult)

        else:
            print("No duplicate files found.")

def main():
    print("-------Marvellous Ifosystems by Piyush khainar-----")

    print("Application name :" +argv[0])

    if (len(argv) !=2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specfic directory and display size of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : Application Absolute_of_Directory Extension")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invaild datatype of input")

if __name__ == "__main__":
    main()
