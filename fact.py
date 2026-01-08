def factorial(n):
    if n < 0:
        return None
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))

result = factorial(num)
if result is None:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial (without recursion):", result)
