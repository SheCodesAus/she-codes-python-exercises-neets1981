# # Python_E.D.3
# # Q1
# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["Crackers", 2.10],
# ["Bacon", 9.00],
# ["Carrots", 0.56],
# ["Oranges", 3.08]]
# orderlist=[]
# sum=0
# for food in  groceries:
#     userinput=float(input ("Enter qty: "))
#     calc= (food[1]) *userinput
#     sum=calc+sum
#     food [1]= calc
#     food_name=food [0]
#     orderlist.append([food_name,calc])
    


# print ("====Izzy's Food Emporium====")
# for i in orderlist:
#     food1=i[0]
#     calc1=i[1]
  
#     print ( "{food1:<15} ${calc1}".format(calc1=calc1,food1=food1)) 

# print ("============================")
# print (f"               {sum}")

# Q2
# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")

# Python_E.D.1

# Exercise Question Sample Answer
# Q1
# number = int(input("Enter a number: "))

# for i in range(1, number+1):
#     print(f"{number} * {i} = {number * i}")



# Q2
# digits= int(input("Enter Number here:"))
# sum=0
# for i in range(1,digits+1):
    
#         # sum= sum+(i+1)
#         sum=sum+i
# else:print (sum)   

# Q3
# random_numbers = [3, 5, 9, 1] 
# random_numbers = [-3, -5, 9, 1] 
# random_numbers = [] 

    # Using sum function as below..
# Sum= sum (random_numbers)
# print(Sum)
    # Using sum for loop as below..
# sum=0
# for i in random_numbers:
#     sum=sum + i
# else: print (sum)
     

# Q4
# mailing_list = [
# ["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"],
# ]
# for i in mailing_list:
#     print (i[0] +": "+i[1])
    
    # Python_E.D.2 - While loop
    
# Q1
# sum=0
# userinput=0
# while userinput !="":
#         sum=sum+(int(userinput)) 
#         userinput= (input("Enter Number : "))  
# else:
#     print (sum)
#alternate way
# input_number = input("Enter a number: ")
# completed_list = []
# print(input_number)
# print(completed_list)
# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")
# print(completed_list)
# print(sum(completed_list))
#alternate way
# sum=0
# while True:
#     userinput= (input("Enter number"))
#     if userinput=="":
#         break
#     else:
#         sum=sum+(int(userinput))
        
        
# print (sum)

# Q2
'''n=(int(input("Enter number to get odd no: ")))
i=1
while i<=n:
    print (i)
    i=i+2
print (n)
'''
# Q-3
'''i= 20
num=int(input("enter a number:"))

while num!=i:
    # num=int(input("enter a number: "))  

    if num<i:
        print("Too low!")
        # num=int(input("enter a number: "))
    elif num>i:
        print("Too high!")
    num=int(input("enter a number: "))  
print("correct!")'''

# userinput=int(input("Enter no. here: "))
# i=userinput
# b=1
# while i>=1:
#     j=1
#     while j<=i:
#         print("*", end='')
#         j=j+1
#     print ()
#     i=i-1

# userinput=int(input("Enter your no : "))
# i=1
# while i<=userinput:
#     j=1
#     while j<=i:
#         print ("*", end='')
#         j=j+1
#     print ()
#     i=i+1

# userinput=int(input("Enter no. here: "))
# i=6

# while i>=1:
#     b=1
#     while b>i:
#         print(" ", end=" ")
#         b=b-1
#     j=1
#     while j<=i:
#             print("*", end='')
#             j=j+1
#     print ()
#     i=i-1
userinput=int(input("Enter no. here: "))
i=1
while i<=userinput:
    b=1
    j=userinput
    while b<i:
            b=b+1
            print(" " * b + "*" * j)
            j=j-1
    i=i+1      
    
# find min number from list and index of it
'''numbers=[4,7,10,2,1]
min_value=numbers[0]
min_location=0
index=0

for num in numbers:
    if num<min_value: # when num is less than min value if yes g ot loop
        min_value=num #save num value minvalue means replace older one
        min_location=index #saving index in min location varible
    index+=1
print(min_value, min_location)'''

