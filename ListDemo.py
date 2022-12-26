print("Demonstration of List")

# Data     : Heterogenous
#Ordered   : YES
#Indexed   : YES
#Mutable   : YES
#Duplicate : YES

data = [11,21,51,101]
data1 = [11,90.80,True, "Hello"]  # Heterogenous

print("Data is Heteogeneous: ",data1)
print("Data is orderd : ",data1)
print("Data at index 2 : ",data[2])
print("Data with duplicate element: ",data)
print("Data after append : ",data)

pritn("List is mutable")
data.append(201)
print("Data after append: ",data)
data.pop()
print("Data after pop : ",data)


