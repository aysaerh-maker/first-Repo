class Mathematics():
    a = 3
    b = 7

    def add(self):
        c = self.a + self.b
        print(c)

    # def __init__(self):
    #     print("this is a constructor")

    def __init__(self,name):
        print("hello, Good Afternoon", name,".")

    def sub(self):
        c = self.b - self.a
        print(c)

    def div(self):
        c = self.a/self.b
        print(c)

    def mul(self):
        c = self.a*self.b
        print(c)

x = Mathematics("Aisha")
#x = Mathematics() # x is the object 
print(x.a)
print(x.b)
x.add()
x.mul()
x.div()
x.sub()

# y = Mathematics() # y is the object 
# y.a = 29
# y.b = 2
# print(y.a)
# print(y.b)
# y.add()
# y.mul()
# y.div()
# y.sub()

#Inheritance
# class Currency_converter(Mathematics): #inherited Mathematics
#     naira = 762325

#     def usd(self):
#         usd = self.naira/1421
#         print(usd)
    
#     def kwd(self):
#         kwd = self.naira/4659
#         print(kwd)

# obj1 = Currency_converter()
# obj2 = Currency_converter()

# obj1.kwd()
# obj2.sub()
# obj1.mul()