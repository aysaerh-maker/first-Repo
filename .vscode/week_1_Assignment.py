#Assignment_1
a = 12
b = 10
m = a & b
print(m)

print(bin(a)) #0b1100
print(bin(b)) #0b1010

#The value is 8. For AND, it's high only when both values are high.

#Assignment_2
result = a | b
print(result)
#for OR, it's high if at least 1 is high. The value for a|b is 14.

#Assignment_3
x = 7
y = 5
print(x^y)
#the result is 1 if bits are different and 0 if they are the same

#SECTION_B
#Assignment_4
n = 3
print(n << 1)
print(n << 2)
# left shift by 1 is multiplying the value(3) by 2**1 and left shift by 2 is multiplying the value by 2**2. Multiply value by 2**no. of positions to shift.

#Assignment_5
n = 20
print(n >> 1)
print(n >> 2)
#divides the number by 2**no. of shifts

#Assignment_6
x = 5
print((x<<2)>>1) #result=10

#SECTION_C
#Assignment_7
a = 8
print(~a)
~a == -(a+1)
b = ~a
print('~a=',b)
print("-(a+1)=",~a)

#Assignment_8
x=0
print(~x)
y=-1
print(~y)
#x=~y and y=~x

#SECTION_D
#Assignment_9
a=6
b=3
print(a&b,'\n',a|b,'\n',a^b,'\n',~a,'\n',a<<1,'\n',a>>1)
#a&b=2 only second bit gives 1. 010=2
#a|b=7 all bits are 1. 111=7
#a^b=5 1st and 3rd bits are diiferent,so, 1. 2nd bits are the the same which gives a 0. outputis 101=5
#~a=-7 (-(6+1))
#a<<1=12 (6*2)
#a>>1=3 (6/2)

#Assignment_10
x=4
y=1
result=x&y<<1
print(result)
#using parentheses
output=x&(y<<1)
print(output) #no difference


#SECTION_E
#Assignment_11
value=13
mask=1
print(value&mask)
#to check bits:
mask=2 #checks 2nd bit
print(value&mask) #2nd bit is 0(not set)
mask = 4 #checks 3rd bit
print(value&mask) #3rd bit is set
mask=8 #checks 4th bit
print(value & mask) #4th bit is set

#Assignment_12
flags = 0
mask=1 #set bit 1
mask_2=4 #set bit 2
print(flags|mask|mask_2)

#Assignment_13
flags=7
print(flags&~1)


#SECTION_F
#Assignment_14
n=16
m=2**4
print(bool(n==m))

#Assignment_15
a=5
b=9
#before swap
print(a,b)
a=a^b
b=a^b
a=a^b
print(a,b) #after swap
