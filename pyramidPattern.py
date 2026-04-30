def pyramidPattern(rows):
    for i in range(1, rows):
        for j in range(1, rows - i):
            print(" ", end = " ")
        for k in range(1, 2 * i):
            print("*", end = " ")
        print()
pyramidPattern(int(input("Enter range of stars : ")))