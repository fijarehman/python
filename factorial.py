n = int(input("enter a number: "))
factorial = 1
i = 1
while i <= n:
 factorial *= i 
 i += 1
print("factorial  of ",n, "is", factorial)