# Normal Function / Named Functions

def Add(No1,No2):
     return No1 + No2


# Lambda Function / Unamed Function
# Lambda parametrs: body

AddFunction = lambda A,B : A + B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Additon using normal function: ",Ans1)
print("Addition using lambda function: ",Ans2)

print("Type of lambda function is: ",type(AddFunction))


  
     
     

     
     