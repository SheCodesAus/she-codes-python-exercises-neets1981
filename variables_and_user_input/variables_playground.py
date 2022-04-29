from cProfile import run
from typing import Type
from unicodedata import name


weather ="rainy"
print (weather)
# Data Types - String is a text data
# Integer numerical data (whole number)
# Float numerical (with decimal)

height =155
weight =55.8
print (type(height))
print (type(weight))
day="saturday"
print(type(day))
message =f"Today is {day}!"
message2= "Today is "+ day
print (message)
print (message2)

#integers
#run distance in
run_dis=1400
run2_dis=1500
#addition
total_dist =run_dis+run2_dis

print(total_dist)

#Addition2
run3_dis=1.7
run4_dis=1.35
print(total_dist)

total_dist =run3_dis+run4_dis
print(total_dist)

#division and multification
print(run_dis/1000)
print (run3_dis*1000)

#divisionis always produce floats
#other calculation depends on the data type
#as long as there is one float, float

# different scenarios
name ="Neeta"
# print(message + run2_dis)
# print (name * run2_dis)
# print (name * run3_dis)
# print (name / run_dis)

#type casting
print (name + str( run_dis))