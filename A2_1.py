
import A2_Module

def main():
     print("value of __name__ from   main is : ",__name__)
     
     print("Enter First Number: ")
     no1 = int(input())
     
     print("Enter Second Number: ")
     no2 = int(input())
     
     Ans = A2_Module.Division(no1,no2)
     
     print("value  is : ",Ans)

if __name__ == "__main__":
     main()
