def Fact_No(iNo):
     
     if iNo ==0:
          return 0
     iFact = 1
     for iCnt in range(iNo):
          iFact = iFact * (iCnt + 1)
          
     return iFact
def main():
     iNo = int(input("Enter number: "))
     print("Factorial of : ",Fact_No(iNo))



if __name__ == "__main__":
    main()
