
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(ord('A')+i),end=" ")
        print("\n")
pattern(5)

