
def Display(No):
     if(No > 0):
          No = No - 1
          Display(No) # Recursive Call
          print(No)          
Display(4)
