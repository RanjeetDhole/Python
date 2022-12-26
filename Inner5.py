
def Substration(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        Output = Function_Name(A,B)  # 200(8,12)
        return Output
    return Inner

def main():
    value1 = int(input("Enter First Number: "))  # 8 
    value2 = int(input("Enter Second Number: "))  #12
    
    New_Function = Decorated_Function(Substration)
    print(New_Function(value1,value2))
    
if __name__ == "__main__":
    main()
    