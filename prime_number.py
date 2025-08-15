def is_prime(num):
    if num < 2:
        return False
    for i in range(2,  int (num **0.5) +1):
        if num % i == 0:
            return False
    return True
# main program 
n = int(input("enter a number to check if it is prime or not : "))
if is_prime(n):
    print(n, " is a prime number")
else:
    print(n, "is not a prime number")
    