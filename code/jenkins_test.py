#new commit main
def ad(a,b):
    if a<b:
        c = a+b
    else:
        c = a-b
    return c

x = int(input("enter a number: "))
y = int(input("enter a number: "))
res = ad(x,y)
print(res)
