import os

def DeleteFile(FileName):
     
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
          
        if(size ==0):
            os.remove(FileName)
        else:
            print("are you want to delete the file ? Y/N")
            option = input()
            if (option == "Y" or option == "N"):
                os.remove(FileName)
            else:
                print("File deletion proces stoped.")
    else:
        print("There is no such file")
                
def main():
     
    print("Enter the file name to delete")
    Name = input()

    DeleteFile(Name)

if __name__ == "__main__":
    main()