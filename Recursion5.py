
def Display(No):
     if(No > 0):
          print(No)
          No = No - 1
          Display(No) # Recursive Call
          
Display(4)
