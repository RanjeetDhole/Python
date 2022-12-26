def main():
    rows = 5
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")

if __name__ =="__main__":
    main()