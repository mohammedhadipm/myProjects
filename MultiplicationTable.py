def multiplicationTable(num):
    for i in range(1,11):
        print(i, "X", num, "=", i*num, "\n")
multiplicationTable(int(input("Enter a number : ")))