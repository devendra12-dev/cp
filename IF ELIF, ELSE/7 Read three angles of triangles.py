a, b, c = map(int, input("Enter three angles: ").split())
if a + b + c != 180 or min(a, b, c) <= 0:
    print("Invalid triangle")
elif 90 in (a, b, c):
    print("Right triangle")
elif max(a, b, c) > 90:
    print("Obtuse triangle")