def MarksGrade(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80 and marks < 90:
        return "B"
    elif marks >= 70 and marks < 80:
        return "C"
    elif marks >= 60 and marks < 70:
        return "D"
    elif marks >= 50 and marks < 60:
        return "E"
    elif marks < 50 and marks >= 0:
        return "Failed"
    else:
        return "Invalid Input!"
print("Grade : ", MarksGrade(int(input("Enter your Marks : "))))
    