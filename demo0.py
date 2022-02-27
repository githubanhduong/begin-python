# Reverse a number in Python
n = int(input("Enter a number: "))
result = ' '
while (n != 0):
    result += str(n % 10) + ' '
    n //= 10
print(result)