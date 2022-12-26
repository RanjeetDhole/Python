# Positional Arguments / keyword argument

def Add1(No1,No2):
     print("value1 of No1: ",No1)
     print("value2 of No2: ",No2)
     return No2 + No1

def Sub1(No1,No2):
     print("value1 of No1: ",No1)
     print("value2 of No2: ",No2)
     return No1 - No2     
     

def main():
     Ans = Add1(10,11)
     print("Addition is: ",Ans)
     
     Ans = Sub1(No1=10,No2=11)
     print("Substraction is: ",Ans)
     
     Ans = Sub1(No2=10,No1=11)
     print("Substraction is: ",Ans)
     
     
if __name__ == "__main__":
     main()
     