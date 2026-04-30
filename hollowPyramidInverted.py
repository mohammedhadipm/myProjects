def hollowPyramidInverted(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end = " ")
        for k in range(1, 2 * i):
            if k == 1 or i == rows or k == 2 * i - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
hollowPyramidInverted(int(input("Enter range of pyramid : ")))