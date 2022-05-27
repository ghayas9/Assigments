a=int(input('Enter First Value : '))
b=int(input('Enter Second Value : '))
c=int(input('Enter Third Value : '))

if a>b and a>c:
    print(f'{a} is greater than {b} and {c}')
elif b>c and b>a:
    print(f'{b} is greater than {a} and {c}')
elif c>b and c>a:
    print(f'{c} is greater then {b} and {a}')
else:
    print('Equal')

if a<b and a<c:
    print(f'{a} is smaller than {b} and {c}')
elif b<c and b<a:
    print(f'{b} is smaller than {a} and {c}')
elif c<b and c<a:
    print(f'{c} is smaller than {b} and {a}')
else:
    print('Equal')


