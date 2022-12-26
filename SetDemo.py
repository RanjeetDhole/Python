print("Demonstration of Set")

# Data     : Heterogenous
#Ordered   : No
#Indexed   : No
#Mutable   : YES
#Duplicate : No

data = {11,21,51,101,21,11}             # Duplicate
data1 = {11,90.80,True, "Hello"}       # Heterogenous

print("First Set Data: ",data)
print("Length of data: ",len(data))
print("Data is Heteogeneous: ",data1)
print("Data is unorderd : ",data1)
# print("Data at index 2 : ",data1[2])
print("Data with  unique element: ",data)


print("Set is mutable")
# Insert Element in Set
data.add(211)

print("Data after insertion data: ",data)

# Remove element
data.remove(211)
print("Data after removal : ",data)

data.discard(201)
print("Data after discard : ",data)


