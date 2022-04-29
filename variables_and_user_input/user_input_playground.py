#input fun always storre string
# name = input("what is your name?")
# print (name)
# input()

# number = input("enter a number ")
# print (int(number)+5)
# print(number +5)

# Writea program that takes two numbers from the user,and outputs the equation 
# representing the multiplication of the two numbers
number1=input("Enter a number ")
number2= input("Enter another number ")
sum= (float (number1)+ float (number2))
print (sum)
equation=(float(number1))* (float(number2))
print (equation)

from re import M

# Writ e aprogram that takes a distance in kilometers from the user,and output the distance in meters
# and centimeters.
kilometers=input("How many kilometers? ")
meters=(float(kilometers)*1000)
Roundmeters=round(meters)
message=f"{Roundmeters}m "
# print km to meters
print (message)
message2= (str(Roundmeters)+"m")
print (message2)
# print km to centimeters
Centimeters= (float(kilometers)*100000)
roundcm=round(Centimeters)
message3=(str(roundcm)+"cm")
print (message3)

# Write a program that takes the users name and height (in centimeters), and outputs a summary sentence.
name= input("What is your name?")
height=input("How tall are you (cms)?")
output= (name +" is " +str(height) +"cm  tall. ")
print (output)


