#4
#4 * 3 * 2 * 1 -> 24

def Add(No):
     Ans = 0 
     if(No <= 0):
          return 1
     else:
          return (No * Add(No - 1))
          

Ret = Add(4)
print("Result is : ",Ret)

