#Module(import python file)
#import assignment_3

#assignment_3.KWD()
# file = open("classfile.txt","w")
# file.write("this is our first txt file")
# file.close()
# file = open("classfile.txt","r")
# print(file.read())
# file.close()

#to write and read
# file = open("classfile.txt","w+")
# file.write("This is the second trial")
# file.seek(0)
# print(file.read())
# file.close()


def calculator():
    operation = input("Choose operator(ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION): ")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    if operation == "DIVISION" and b == 0:
        print("Math Error: Cannot divide by zero.")
        return
    operator = {
        "ADDITION": a+b,
        "SUBTRACTION": a-b,
        "MULTIPLICATION": a*b,
        "DIVISION":a/b
    }
    result = operator[operation]
    if operation in operator:
        print(result)
    else:
        print("invalid input")

calculator()

#TEMPERATURE CONVERTER
C = float(input("Enter temp in degrees Celsius: "))
F = (C*9/5)+32
print(F,"degrees Fahrenheit")

#NUMBER GUESSING GAME
correct_number = 7
guess = int(input("Guess the number: "))
if guess == 7:
    print("Congratulations, you win!!!")
else:
    print("Oops! Try again.")

