# name='Ali'
# surname='muhammad'
# age='40'
# # print('ATBU just hired a new staff with first name ',name,' and surname ', surname,' and aged ',age,' years old') #use space before quotation
# #using formatted string
# information=f"ATBU just hired a new staff with first name {name} and surname  {surname} and aged {age} years old"
# print(information)
# print(type(information))
# print('make a choice of dish you want')
# name=input('Enter your name: ')
# choice=input('What will you eat: ')
# Dish=f"dear {name}, your {choice} on the way, enjoy"
# print(Dish)

#Age calculator
# Year_of_Birth=input('What year were you born?: ')
# current_year=input('What year are we: ')
# Age=int(Year_of_Birth)-int(current_year)
# print(Age)
Year_of_Birth=int(input('What year were you born?: '))
current_year=int(input('What year are we: '))
Age=current_year-Year_of_Birth
print(f'You are {Age} years old')
