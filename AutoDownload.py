import requests
import re
from urllib.parse import urlparse
from sys import *
import os


def is_downloadable(url):
    h = requests.head(url,allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    
    if 'text' in content_type.lower():
        return False
    
    if 'html' in content_type.lower():
        return False
    
    return True

def get_filename_from_cd(cd):
    a= urlparse(cd)
    return os.path.basename(a.path)

def MarvellousDownload(url):
    allowed = is_downloadable(url)
    
    if allowed:
        try:
            res = requests.get(url,allow_redirect=True)
            res.raise_of_status()
            filename= get_filename_from_cd(url)
            fd = open(filename,"wb")
            
            for buffer in res.iter_content(1024):
                fd.write(buffer)
            
            fd.close()
            return True
        except Exception as E:
            return False
    else:
        return False

def main():
    print("----By:Ranjeet Dhole----")
    
    print("Application Name: " +argv[0])
    
    if(len(argv)==2):
        if (argv[1]=="-h") or (argv[1]=="-H"):
            print("This Script is used download file")
            exit()
            
        if(argv[1]=="-u") or (argv[1]=="-U"):
            print("usage: ApplicationName Name")
            exit()
    
    url = 'https://www.google.com/search?q=jpeg+image&oq=&aqs=chrome.3.35i39i362l8.611920546j0j15&sourceid=chrome&ie=UTF-8#imgrc=1p7Pqah9uSgJYM'
    
    result = MarvellousDownload(url)
    
    if result:
        print("File Sucessfully downlaod")
    else:
        print("Failed to downlaod")
        
if __name__ == "__main__":
    main()