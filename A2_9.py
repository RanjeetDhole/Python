def Check_Number(iCnt):
    if iCnt == 0:
        return 0

    iDigitCount = 0
    while iCnt != 0:
        iCnt = int(iCnt) / 10
        if iCnt != 0:
            iDigitCount = iDigitCount + 1

    return iDigitCount


def main():
    iCnt = int(input("Enter number : "))
    print("The number of digits in {} is {}".format(iCnt, Check_Number(iCnt)))


if __name__ == "__main__":
    main()