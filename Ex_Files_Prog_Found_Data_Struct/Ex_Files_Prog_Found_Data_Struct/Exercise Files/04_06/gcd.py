

#gcd of two numbers
a=int(input("please but num :: "))
b=int(input("please but num :: "))

def gcd(a ,b) :
    while (b != 0):
        t=a
        a=b
        b=t % b
    return a

print(gcd(a,b))
