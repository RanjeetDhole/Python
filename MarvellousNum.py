def checkFactor(iCnt,iNo):
    if iNo == 0:
        return False

    if iNo % iCnt == 0:
        return True
    else:
        return False


def checkPrime(iNo):
    if iNo == 0 or iNo == 1:
        return False

    iCnt = 2
    while iCnt <= iNo:
        if checkFactor(iCnt, iNo) == True:
            break
        iCnt = iCnt + 1

    if iCnt == iNo:
        return True
    else:
        return False


def Addition(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + data[i]

    return sum