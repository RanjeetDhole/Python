def ChkNum(No):
     if No > 0:
          print("Number are positive")
     else:
          print("Number are Negative")

def main():
     print("enter the number")
     value = input()
     
     ChkNum(int(value))
     
  
if __name__ == "__main__":
     main()