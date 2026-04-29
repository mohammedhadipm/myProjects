def SimpleInterest(P, R, n):
    SI = (P * R * n) / 100
    return SI
print("Simple Interest", SimpleInterest(*map(int, input("Enter Principal Amount, Interest rate and Number of years in order : ").split())))