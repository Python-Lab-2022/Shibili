def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
    return
n=int(input("enter a number:"))
print("all factors of",n,"are")
factors(n)
