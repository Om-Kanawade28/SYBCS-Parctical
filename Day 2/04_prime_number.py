n = int(input("Enter the Number:-"))
for i in range(2,n):
    if n%i==0:
       isprime = False
    else:
        isprime = True
    
if isprime == True:
    print(n,"is prime number")
else:
    print(n,"is not prime number")