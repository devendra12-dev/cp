A, B = map(int, input("Enter two numbers: ").split())
result = 1
for _ in range(B):
    result *= A
print(f"{A}^{B} = {result}")