nterms =  int(input("enter the Numbera:-"))
n1,n2 = 0,1
count = 0

if nterms <= 0:
    print("Invailed number")
else:
    print("Fibonacci series:-")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1