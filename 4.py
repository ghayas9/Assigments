def finddividor(x):
    d=[]
    for i in range(1,x):
        if x%i==0:
            d.append(i)
    return d

def check_perfect(x):
    if sum(finddividor(x))==x:
        return True
    else:
        return False

def isprime(x):
    if x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

dd=[]
i=1
while len(dd)<5:
    if check_perfect(i):
        dd.append(i)
    i+=1

print(dd)


