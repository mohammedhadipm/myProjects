def rightAngledTriangleInverted(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
rightAngledTriangleInverted(int(input("Enter range of stars : ")))