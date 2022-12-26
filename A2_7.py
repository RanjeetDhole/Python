def main():
    rows = 5
    for i in range(1,rows):
        for j in range(1, rows+1):
            if i >= rows:
                print(i, end=' ')
            else:
                print(j, end=' ')
        print("\r")


if __name__ == "__main__":
    main()