def numRightAngledTriangleInverted(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()
numRightAngledTriangleInverted(int(input("Enter size of triangle : ")))
