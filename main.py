my_name=input('your name?')

my_age=input('your age?')

print(f'My name is {my_name} and I am {my_age} years old')

first_number=int(input('choose the first number'))

secound_number=int(input('choose the the secound number'))

operation=input('choose a sing to do the operation')

if operation=='+':
    print(first_number + secound_number)

elif operation=='-':
    print(secound_number- first_number)

elif operation=='*':
    print(first_number*secound_number)

elif operation=='/':
    print(first_number/secound_number)

else:
    print('the operation is not valid')

bus_capacity=48  

people_inbus=int(input('how many people is in the bus?'))

waiting=int(input('how many people are waiting?'))

ampty_seatas = bus_capacity - people_inbus

if ampty_seatas>=waiting :
    print(f'ther are ampty_seatas{ampty_seatas}')

elif ampty_seatas<people_inbus:
    print('oops the bus is full')