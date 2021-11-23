x = int(input("Enter the number you want your Fibonacci series to run= "))
p, q = 0, 1
count = 0
print("FIBONACCI SERIES UPTO",x,"TERMS IS:")
while count < x:
    print(p)
    t =p + q
    p = q
    q = t
    count += 1
