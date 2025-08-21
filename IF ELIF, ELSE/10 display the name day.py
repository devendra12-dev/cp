days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
n = int(input("Enter a number (1-7): "))
print(days[n-1] if 1 <= n <= 7 else "Invalid input")