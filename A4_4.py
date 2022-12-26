import functools

CheckEven = lambda no: (no % 2 == 0)
Product = lambda no: no * no
Addition = lambda no1,no2: no1 + no2

def main():
     Arr = list()
     
     print("Enter the size of list")
     size = int(input())
     
     for iCnt in range(size):
          print("Enter element",iCnt + 1," in list")
          Arr.append(int(input()))
          
     print("list is ",Arr)
     
     data = list(filter(CheckEven,Arr))
     print("After filter",data)
     
     data = list(map(Product,data))
     print("After Product",data)
     
     data = functools.reduce(Addition,data)
     print("Sum is ",data)
     
     
if __name__ == "__main__":
     main()