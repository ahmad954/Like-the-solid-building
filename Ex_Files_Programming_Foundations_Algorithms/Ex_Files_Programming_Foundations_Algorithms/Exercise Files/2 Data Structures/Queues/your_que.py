from collections import deque
#ahmad muhmmad fathi
x=int(input("put how many numbers you want to add ; "))

lit = deque()
for i in range(x):
    y=int(input("your num :: "))
    lit.append(y)
    print(lit)


pop=input("if you want to pop enter y or Y :")

if pop == "Y"  :
    lit.popleft()
    print(lit)

print('thank you for using my app :)')