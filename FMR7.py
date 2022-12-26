from functools import reduce

CheckEven = lambda No: (No % 2 == 0)  # using Lambda Function

Doubles = lambda No: No*2     # using Lambda Function

Sum = lambda A,B: A+B      # using Lambda Function


def main():
     
     print("Enter number of elements you want to enter: ")
     iSize = int(input())
     
     Data_Input = []
     print("Please enter the data")
     for iCnt in range(0,iSize,1):
          Value = int(input())
          Data_Input.append(Value)
          
     
     print("Data is: ",Data_Input)     
     
     Data_Filter = list(filter(CheckEven, Data_Input))
     
     print("Data After Filter is: ",Data_Filter)
     
     
     Data_Map = list(map(Doubles, Data_Filter))
     print("Data after map is: ",Data_Map)

     
     Output = reduce(Sum,Data_Map)
     print("Result After Reduce is: ",Output)
     
     
if __name__ == "__main__":
     main()