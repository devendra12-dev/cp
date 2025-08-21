A = int(input("Enter a number: "))
original = A
reversed_num = 0
while A > 0:
    digit = A % 10
    reversed_num = reversed_num * 10 + digit
    A //= 10
if original == reversed_num:
    print("Palindrome")
else:
    print("Not palindrome")
