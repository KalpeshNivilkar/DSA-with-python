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





# print("Welcome to BMI Measuring")
# print("BMI calculator")

# def Bmi_cal(weight,height_cm):
#     height_m = height_cm / 100
#     bmi = weight / (height_m * height_m)
#     round_bmi = round(bmi,2)
#     print(f"your BMI measuring is done!")
#     print(f"your BMI is : {round_bmi}")
                                                                   #    BMI calculator
#     if round_bmi >25:
#         print("you are not fit!")
#     elif round_bmi >15 and round_bmi<24:
#         print("you are fit")
#     elif round_bmi <15:
#         print("you are underweight")
# # user input
# w = int(input("Enter your body weight : "))
# h = int(input("Enter your height : "))
# # function call
# Bmi_cal(w,h)


# print("finding Factorial number!")
# def cal_f(num):
#     fact=1
#     for i in range(1,num+1):                                         #factorial number
#         fact *= i
#     print(f"the factorial number is :{fact}")

# n=int(input("Enter any number :"))
# cal_f(n)



# print("printing the given number is even or odd")

# def check(num):
#     if num % 2 == 0:
#         print("the given num is even")
#     elif num % 3 == 0:                                                   #printing the given number is even or odd
#         print("the given num is odd")
#     else:
#         print("gives valid input")
#         print("type again")
# #user input
# n=int(input("Enter any number: "))
# check(n)

print("sending otp on mobile number")
def otp_send(mobile_no):
    print(f"sending otp on mobile number :{mobile_no}")

number = int(input("enter your mobile number :"))
otp_send(number)