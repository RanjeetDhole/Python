from sys import *
import webbrowser
import re
from urllib.request import urlopen

def is_connected():
    try:
        urlopen('http://google.com')
        return True
    except Exception as err:
        return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(/),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str,new=2)
                
    
def main():
    print("----By:Ranjeet Dhole----")
    
    print("Application Name: " +argv[0])
    
    if(len(argv)!=2):
        print("Error: Invalid Number of Argument")
        exit()
        
    if (argv[1]=="-h") or (argv[1]=="-H"):
        print("This Script is used open URL which are written in one file")
        exit()
        
    if(argv[1]== "-u") or (argv[1]=="-U"):
        print("usage: ApplicationName Name_of_file")
        exit()
        
    try:
        connected = is_connected()
        
        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to internet")
            
    except ValueError:
        print("Error: Invalid datatype of input")
        
    except Exception as E:
        print("Error: Invalid input",E)

    
if __name__ == "__main__":
    main()