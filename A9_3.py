import os
from sys import *

def Create_Copy(path):
    
    print("The path is : ",path)
    
    cObj = open(argv[1],'r')
    copy_content = cObj.read()
    print("copy content",copy_content)
    fObj=open(argv[2],'w')
    fObj.write(copy_content)
    
def main():
    print("File Name",argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of arguments")
    try:
        Create_Copy(argv[1])
    except Exception as E:
        print("Error : Invalid Input")
            
if __name__ == "__main__":
    main()