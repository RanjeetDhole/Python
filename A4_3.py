import functools
CheckNumber = lambda no: (no >= 70 and no <= 90)
Addition = lambda no: no + 10
Product = lambda no1,no2: no1 * no2

def main():
     Arr = list()
     
     print("Enter the size of list")
     size = int(input())
     
     for iCnt in range(size):
          print("Enter element",iCnt + 1," in list")
          Arr.append(int(input()))
          
     print("list is ",Arr)
     
     data = list(filter(CheckNumber,Arr))
     print("After filter",data)
     
     data = list(map(Addition,data))
     print("After Increment",data)
     
     data = functools.reduce(Product,data)
     print("data is ",data)
     
     
if __name__ == "__main__":
     main()