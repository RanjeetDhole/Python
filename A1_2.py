def ChkNum(No):
     if No % 2 == 0:
          print("Number are even")
     else:
          print("Number are odd")

def main():
     print("enter the number")
     value = input()
     
     ChkNum(int(value))
     
  
if __name__ == "__main__":
     main()