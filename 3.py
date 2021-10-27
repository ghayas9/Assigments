a=input('Enter anything : ')
c=''
for i in a:
    if(i.lower() not in c and i.upper() not in c):
        print(f""" {i} = Total  : {a.lower().count(i)} 
    | Lower : {a.count(i.lower())} 
    | Upper : {a.count(i.upper())}""" ,end='\n\n')
        c+=i

d=''
for i in a:
    if i not in d:
        print(f'{i}   {a.count(i)}')
        d+=i