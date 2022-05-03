
# # 3 elements
# # #lists
# # 0 index
characters =["a", "b", "c"]
# append d in list 
print (characters)
if "d" in characters:
    print("good")
else:
    characters.append("d")
    print (characters)

# Return no.of list
print (len(characters))
    



# #grab first element
# print (characters[0])
# # grab last elemtn
# print (characters[-1])
# # strating index included, stopping at 2 so print 0 and 1 index
# print(characters[0:2])
# #delte by using  pop
# print (characters.pop())
# #remove index 1
# print (characters.pop(1))
# #remove a but wont return so u need to print
# print (characters.remove("a"))
# print (characters)
# # ------
# print (characters)
# print (type(characters))
# characters.append("d")
# # add more than 1 element
# characters.extend(['e', 'f'])
# # add g before index 1
# characters.insert(1,"g")
# print (characters)

chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
print (chilli_wishlist[-1])
chilli_wishlist[1] ='Carrot'
print (chilli_wishlist)
# Stat at 1 to 4 and skip 2
print (chilli_wishlist[1:2:2])
print (chilli_wishlist[2:4])

# print -3 posititon
print(chilli_wishlist[-3])

asli = [[3,5], ["blue", "pink"]]
# print(asli[0])
# print (asli[1])
# # grab pink 
# print (asli[1][1])