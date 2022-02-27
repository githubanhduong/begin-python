#check number is prime or not
n = 17  #int(input("Enter a number: "))
flag = True

if (n < 2):
    flag = False
elif (n == 2):
    flag = True
elif (n % 2 == 0):
    flag = False
else:
    for i in range(3, n, 2):
        if (n % i == 0):
            flag = False

if (flag == True):
    print(" is a prime number", n)
else:
    print(" is not a prime number", n)
