def PassFail(marks):
    if marks >= 50 and marks <= 100:
        print("Passed")
    elif marks < 50 and marks >= 0:
        print("Failed")
    else:
        print("Invalid Input")
PassFail(int(input("Enter your Marks : ")))
