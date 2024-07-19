num = int(input("Enter a number:-"))
factorial = 1
if num < 0:
    print("negative number")
elif num == 0:
    print("number is zero")
else:
    for i in range(1,num+1):
        factorial = facctorial*i;
    print("the factorial of ",num,"is",factorial)
    