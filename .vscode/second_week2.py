# x=int(input("Enter any number here"))

# if x<0:
#     x=0
#     print('Negative changed to Zero')
# elif x==0:
#     print('number is zero')
# elif x>0:
#     print('x is greater than zero')

# print(f"{x} is the number") #formatted strings

#.format method````````````
name = input('Enter your name here: ')
Age = int(input('Enter your age: '))
# height=float(input('Enter your height here: '))
present=bool(input('are you in class?(True/false): '))
# print(f"My name is {name}, I am {Age} years old, {height}ft tall and {present}, I am in class.")
print('My name is {} and i am {} years old'.format(name, Age))
# list=[name,Age,height,present]
# for i in list:
#     print(i)
    


