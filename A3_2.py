def Maximum(Data):
     iMax = 0
     for i in range(len(Data)):
          if Data[i] > iMax:
               iMax = Data[i]
     return iMax

def main():
    Arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1)
        Arr.append(int(input()))

    print("List is ", Arr)
    ret = Maximum(Arr)
    print("Maximum Number is ", ret)


if __name__ == "__main__":
    main()