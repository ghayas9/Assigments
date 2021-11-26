import itertools

f=open('password.txt','x')

inp=input('Enter Your key : ')
mi=int(input('Enter min len : '))
mx=int(input('Enter max len : '))

for l in range(mi,mx+1):
    for i in itertools.product(inp,repeat=l):
        x=''.join(i)
        f.write(x+'\n')





