def sumOfOddNumbers(limit):
    total = 0
    for i in range(1, limit+1):
        if i % 2 == 1:
            
            total = total + i
    return total
x = int(input("Enter a limit : "))
print("Sum of odd numbers = ", sumOfOddNumbers(x))