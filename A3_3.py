def Minimum(Data):
     iMini = Data[len(Data)-1]
     for i in range(len(Data)):
          if Data[i] < iMini:
               iMini = Data[i]
     return iMini

def main():
    Arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1)
        Arr.append(int(input()))

    print("List is ", Arr)
    ret = Minimum(Arr)
    print("Minimum Number is ", ret)


if __name__ == "__main__":
    main()