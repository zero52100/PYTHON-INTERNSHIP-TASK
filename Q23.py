def tocheck_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
result = tocheck_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
