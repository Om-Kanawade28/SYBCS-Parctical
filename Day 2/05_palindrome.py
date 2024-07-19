n = int(input("Enter the number:-"))
temp = n
reverse = 0
while temp >0 :
    reminder = temp%10
    reverse = reverse*10 + reminder
    temp = temp//10
    
if n == reverse:
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")
    
