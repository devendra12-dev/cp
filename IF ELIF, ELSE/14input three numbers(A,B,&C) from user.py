
a = int(input("Enter first number (A): "))
b = int(input("Enter second number (B): "))
c = int(input("Enter third number (C): "))

if a <= b and a <= c:
    print("Minimum number is", a)
elif b <= a and b <= c:
    print("Minimum number is", b)
else:
    print("Minimum number is", c)