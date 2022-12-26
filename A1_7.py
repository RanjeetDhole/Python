def ChkNum(No):
     if No % 5 == 0:
          print("True")
     else:
          print("False")

def main():
     print("enter the number")
     value = input()
     
     ChkNum(int(value))
     
  
if __name__ == "__main__":
     main()