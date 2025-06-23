# string :  String is data type that stores a sequence of characters.
        #   method 1 ] slicing : 
        #                      str[ starting_idx : ending_idx ] #ending idx is not included
        #   method 2 ] count :
        #                     used to count the sting also single character 
        #   method 3 ] split():
        #                     used to split the string 
        #   method 4 ] strip():
        #                     used to removed extra empty space taken by string element
        #   method 5 ] ASCII value : ord()

# printing lenght of string 

name = "kalpesh nivilkar"
nameLenght = len(name)
print(nameLenght)
# output will be : 16 

# accessing index element 

access = name[1]
print(access)
# output will be : a 

# slicing of list 

# name [starting index : ending index]   ........syntax

sliceName = name[0 : 7]
print(sliceName)
# output will be : kalpesh 


# example]  WAP to find the occurrence of ‘$’ in a String.

# text = input("enter any text which conatain $ :")

# counttext = text.count("$")
# print(counttext)

            # using another way


# msg = str(input("enter the msg which contain $ : "))
# count = 0 

# for i in (msg):
#     if str == "$":
#         count += i

# print(count)



# split text 

mySelf = "kalpesh subhash nivilkar"
print(mySelf.split())
# output will be : ['kalpesh', 'subhash', 'nivilkar']

mySelf = "kalpesh subhash nivilkar"
print(mySelf.split("a"))
# output will be : ['k', 'lpesh subh', 'sh nivilk', 'r']



# strip method

yourSelf = "  adinath   "
print(yourSelf)
# output will be :   adinath   

print(yourSelf.strip())
# output will be :adinath  


# ASCII value 

me = "a"
print(ord(me))


