def Reverse(iNo):
     for iNo in range(iNo,0,-1):
          print(iNo,end= ' ')
     
          
def main():
     print("Enter the number")
     value = input()
     Ans = Reverse(int(value))
     
if __name__ == "__main__":
     main()