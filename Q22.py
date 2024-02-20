def to_check(num):
    if num <= 0:
        return False
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num

sqr=int(input("Enter the number to check perfect square :"))
if to_check(sqr):
    print(f"{sqr} is a perfect number.")
else:
    print(f"{sqr} is not a perfect number.")



