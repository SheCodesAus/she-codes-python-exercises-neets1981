
#Defnition
'''def hello():
    print ("hello world")
    return 5
    
print (hello())
result=hello()
print (result)
'''
from tkinter import Y


name= "Asli" # global variable
def add(number1,number2):
    result= number1+number2
    #number1 and number 2 is local variable
    return result

add(5,2)
sum=add(5,8)
print (sum)
# to print result 
print (add(5,3))

def multiply (number):
    result= 3*number
    return result
print (multiply(10))

def calculate(x,y):
    total = x + y
    mean=total/2
    return mean
abc=(calculate(10,20))
print (abc)

#Q1

''''def temp_in_f(convert_f):
    tem_in_celsius =(convert_f-32)*5/9
    return tem_in_celsius

print (temp_in_f(0))
print (temp_in_f(32))
print (temp_in_f(350))
'''

def digit (num):
    if num % 2==0:
        return (False)
    else: return (True)
    # return (num)

a = (digit(3))
print (a)
