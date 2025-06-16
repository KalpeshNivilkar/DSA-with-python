# def fun():                                                #simple pyhton function program
#     print("hello Kalpesh")

# fun()

# name_ls =["pratik","akshay","sagar"]
# def print_name_ls(my_ls):                                   #printing length of list
#     print(len(my_ls))

# print_name_ls(name_ls)


# name_ls =["pratik","akshay","sagar"]                          # printing ls in inline
# def print_inline(ls):
#     print(ls,end=" ")

# print_inline(name_ls)

# usd_amt = int(input("enter the USD amt :$"))
#                                                               #convert usd to inr
# def usd_to_inr(money):
#     print(money*82)
   
# usd_to_inr(usd_amt)


print("BMI Calculator")

def measure(weight,height_cm):
    height_m = height_cm/100
    BMI = weight / (height_m*height_m)
    print(BMI)

measure(60,170)