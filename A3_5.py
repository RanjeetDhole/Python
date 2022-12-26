import MarvellousNum

def ListPrime(data):
    Brr = list()
    iCnt = 0
    for iCnt in range(len(data)):
        if MarvellousNum.checkPrime(data[iCnt]):
            Brr.append(int(data[iCnt]))

    print("Prime number list ", Brr)

    iRet = MarvellousNum.Addition(Brr)

    return iRet

def main():
    Arr = list()

    print("Enter the size of list")
    size = int(input())

    for iCnt in range(size):
        print("Enter element ", iCnt + 1, " in list")
        Arr.append(int(input()))

    print("List is ", Arr)

    iRet = ListPrime(Arr)
    print("Addition is ",iRet)


if __name__ == "__main__":
    main()