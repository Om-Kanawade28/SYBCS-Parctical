n = int(input("Enter the Number:-"))
temp = n
sum1 = 0
while temp > 0:
    digit = temp%10
    sum1 = digit*3 + sum1
    temp = temp//10
    
if n==sum1:
    print(n,"Armstrong number")
else:
    print(n," not Armstronge number")