
def Display(No):
     if(No > 0):
          
          print("Hello")
          No = No - 1 
          Display(No)  #  Recursive Function Call
        
Display(4)  # Function Call