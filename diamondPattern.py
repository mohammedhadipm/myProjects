def diamondPattern(rows):
    for i in range(1, rows):
        for j in range(rows - i):
            print(" ", end = " ")
        for k in range(1, 2 * i):
            print("*", end = " ")
        print()
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end = " ")
        for k in range(1, 2 * i):
            print("*", end = " ")
        print()
diamondPattern(int(input("Enter range of stars : ")))