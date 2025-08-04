n = int (input("enter how  many terms you want : "))
a,b = 0,1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b 
    b = c
    count += 1