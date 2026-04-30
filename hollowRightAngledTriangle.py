def hollowRightAngledTriangle(rows):
 for i in range(1, rows + 1):
  for j in range(1, i + 1):
   if j == 1 or i == 1 or i == rows or j == i:
    print("*", end = " ")
   else:
    print(" ", end = " ")
  print()
hollowRightAngledTriangle(int(input("Enter range of triangle : ")))