
A = int(input("Enter first angle (A): "))
B = int(input("Enter second angle (B): "))
C = int(input("Enter third angle (C): "))

if A > 0 and B > 0 and C > 0 and (A + B + C == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")