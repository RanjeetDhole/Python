import pywhatkit

def main():
    print("Type a number to message:")
    number = input()
    
    print("Type a message:")
    message = input()
    
    pywhatkit.sendwhatmsg_instantly(number, message, 5)
    
if __name__ =="__main__":
    main()
