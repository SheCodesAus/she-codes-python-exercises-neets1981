
# Q1



foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
print (foods[0])
print (foods[2])
print (foods[-1])
print (foods[0:3])
print (foods[-3:])
# print 2nd item of 6th 
print (foods[6][2])

# Q2
# mailing_list = [["Chilli", "chilli@thechihuahua.com"],["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Ivy", "noreply@goldendreamers.xyz"],]
# print (mailing_list[0][0]+": "+mailing_list[0][1])
# print (mailing_list[1][0]+": "+mailing_list[1][1])
# print (mailing_list[2][0]+": "+mailing_list[1][1])
# print (mailing_list[3][0]+": "+mailing_list[1][1])

# Q3
namelist=[]
entername1=(input("Enter name: "))
entername2=(input("Enter name: "))
entername3=(input("Enter name: "))
namelist.extend([entername1, entername2, entername3])
print (namelist)