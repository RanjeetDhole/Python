def main():
    try:
        
        print("Enter first number")
        No1 = int(input())
        
        print("Enter second number")
        No2 = int(input())
        Ans = No1 / No2
        print("Division is: ",Ans)
    
        
    except ZeroDivisionError:
        print("Inside Zero Division Error")
    
    except ValueError:
        print("Inside value error")
        
    except Exception:
        print("Inside value error")
        
        
    finally:
        print("Inside finally block")
        
        
if __name__ == "__main__":
    main()