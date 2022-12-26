def Frequency(Data,Value):
     iCnt = 0
     for iNo in range(len(Data)):
          if Data[iNo] == Value:
               iCnt = iCnt + 1
     return iCnt

def main():
    Data = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1)
        Data.append(int(input()))

    print("List is ", Data)
    print("Enter the number you want to check the frequency")
    Value = int(input())
    iRet = Frequency(Data,Value)
    print("Frequency of {} in list is = {}".format(Value,iRet))
    
    


if __name__ == "__main__":
    main()