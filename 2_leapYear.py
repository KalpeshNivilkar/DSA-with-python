

"""""def toCheckIsLeapOrNot(year):

    if (year % 400 == 0) and (year % 100 == 0):
        print(year,"This is leap year")
    elif(year % 4 == 0) and (year % 100 != 0):
        print(year,"This is leap year")
    else:
         print(year,"This is not leap year")
         
year = int(input("Enter the Year: "))
toCheckIsLeapOrNot(year)"""""
        

def leapYear(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print(year,"this is leap year")
    elif(year % 4 == 0) and (year % 100 != 0):
        print(year,"this is leap year")
    else:
        print(year,"this is not leap year")

year = int(input("enter the year : "))
leapYear(year)