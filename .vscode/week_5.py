#OOP practice Tasks(progressive)

class Student_Profile():
    def __init__(self, name, matric_number, course):
        self.name = name
        self.matric_number = matric_number
        self.course = course
        
    def introduction(self, name, matric_name, course):
        print(" Hi, Good morning. I am", self.name,"," "with matric_number", self.matric_number,"," " and a student of", self.course,".")
        

    def display(self):
        print(self.name)
        print(self.matric_number)
        print(self.course)
        
student1 = Student_Profile("Aisha G", "PGS/24-25/11132", "Embedded AI")
student2 = Student_Profile("Natsu Dragneel", 293038, "Fairytail")

student1.introduction()
print(student1.name)
print(student1.matric_number)
print(student1.course)

print(student2.name)
print(student2.matric_number)
print(student2.course)

# #Encapsulation

#Inheritance
class School_Staff():

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def role(self):
        return "Staff"

class Teacher(School_Staff):
    def role(self):
        return "Subject Teacher"
    
class admin(School_Staff):
    def role(self):
        return "Admin"   

staff1 = School_Staff("Sidi Auta", "X010")
staff2 = Teacher("Austin Joseph", "X110")
staff3 = admin("Balarabe Garba", "X007")
staff4 = Teacher("Hauwa Ahmad", "X070")
staff5 = School_Staff("Sidi Auta", "X091")

print(staff1.role())
print(staff2.role())
print(staff3.role()) 
 


        