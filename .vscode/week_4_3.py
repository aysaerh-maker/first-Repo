# print("You came across a dungeon during a quest.\nMake a decision.")
# decision = input("Enter the dungeon or turn back?")
# if decision == "Enter the dungeon":
#     print("you win the quest!")
# elif decision == "turn back":
#     print("Game Over")
# else:
#     print("decision Error")
# class Football_Match():
#     Arsenal = 0
#     Man_U = 0

#     def __init__(self,name):
#         print(f"Hello {name}, Kick Off")

#     def Arsenal_score(self):
#         self.Arsenal+=1
    
#     def Man_U_score(self):
#         self.Man_U+=1

#     def check_scores(self):
#         print(f"Arsenal: {self.Arsenal}\nMan_U: {self.Man_U}")

# match1 = Football_Match("Home") #add "" always in the parenthesis
# match2 = Football_Match("Away")

# match1.check_scores()
# match1.Man_U_score()
# match1.Man_U_score()
# match1.Man_U_score()
# match1.check_scores()

# match2.Arsenal_score()
# match2.Arsenal_score()
# match2.Man_U_score()
# match2.Man_U_score()
# match2.Man_U_score()
# match2.check_scores()

#POLYMORPH
class polymorph():

    def mul(self,*args): #self in () and , for additional parameters. add * for multiple parameters
        a = 1
        for i in args:
            a*=i
        print(a)
obj1 = polymorph()
obj1.mul(2)
obj1.mul(5,7)
obj1.mul(23,45,4,3,1,10,11,29)

print(len('Aisha'))
print(len([7,'Aisha','Abdullahi',4,'Gwaram',10,38])) #example of polymorph

class Tax_ID():

    def __init__(self, name, age, salary):
        self.name =name # no underscore: public attribute
        self._age = age # with 1 underscore: protected attribute
        self.__salary = salary # with double underscore: private attribute
    def some(self):
        print(self.name)
        print(self._age)
        print(self.__salary)

x = Tax_ID("Aisha_G", 30, 27000000)
print(x.name)
print(x._age)
print(x.__salary)
