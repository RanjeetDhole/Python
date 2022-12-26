Power = lambda no: no * no

def main():
    print("Enter the number")
    no = (int(input()))
    
    print("Power of number {} is {}".format(no,Power(no)))
    
    
if __name__ == "__main__":
    main()