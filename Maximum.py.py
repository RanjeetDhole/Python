#Application to findout the maximum number

def Maximum(No1,No2):
     if No1 > No2:
          return No1
     else:
          return No2
     
def main():
     print("enter first number")
     value1 = input()
     
     print("Enter second number")
     value2 = input()
     
     Ans = Maximum (int(value1),int(value2))
     
     print("Largest number is: ",Ans)

if __name__ == "__main__":
     main()