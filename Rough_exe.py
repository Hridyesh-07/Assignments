'''
c=input('Celsius: ')
c=float(c)
f=(c * 9/5) + 32
[print('Farenheit: ',f)]


#Farenheit ------>Celsius
f=input('Farenheit: ')
f=float(f)
c=(f-32)* 5/9
print('Celsius:', c)
'''

'''
#Simple interest calculator
#Eqn: Pnr/100

p=input('p: ')
n=input('n: ')
r=input('r: ')
p=int(p)
n=int(n)
r=int(r)

SI=(p*n*r)/100
[print('Simple Interest is: ',SI)]
'''
'''

Age=int(input('Enter the age: '))
if (Age>=18):
    print('Elidgible for voting')
else:
    print('Not elidigble for voting')
print('Thank You:)')
'''

'''
Value_1=int(input('Enter Value 1: '))
Value_2=int(input('Enter Value 2: '))
Operator=input('Choose the operator (+,-,*,/): ')

if Operator=='+':
    print(Value_1 + Value_2)
elif Operator=='-':
    print(Value_1 - Value_2)
elif Operator=='*':
    print(Value_1 * Value_2)
elif Operator=='/':
    print(Value_1 / Value_2)
else:
    print('None')
print('Thank You:)')
'''
