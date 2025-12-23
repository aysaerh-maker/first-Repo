# score=float(input('Enter your score: '))
# if score >= 70:
#     print("A")
# elif score >= 60:
#     print("B")
# elif score >= 50:
#     print("C") 
# else:
#     print("F") 

name=input('Enter your name: ')
faculty=input('Enter your faculty: ')
department=input('Enter your department: ')
level=int(input('Enter your level: '))
# print(f"I am {name}, a student of faculty of {faculty}, department of {department} and currently in {level}L.")          
# print("I am {}, a student of faculty of {}, department of {} and currently in {}L".format(name, faculty, department, level))    
# print("I am {1} a student of faculty of {2},department of {3}and currently in {0}L".format(level, name, faculty, department))
if department =="Mechatronics":
    print(f'{name} is an engineering')#include f or use .format
else:
    print('not an engineering student')

