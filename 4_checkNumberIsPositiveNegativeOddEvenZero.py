# given number check is positive,negative,odd,even,zero

"""""def checkNumber(n):
    if n == 0:
        print(n,"it is zero")
    elif n < 0:
        print(n,"it is negative ")
    else:
        print(n,"it is possitive")

        if n % 2 == 0:
            print(n,"it is even")
        else:
            print(n,"it is odd ")

(checkNumber(28))"""""


def checkNumber(num):
    if num == 0:
        print("this is zero")
    if num < 0:
        print("this is negative number")
    else:
        print("this is positive number")

        if num % 2 == 0:
            print("this is even number")
        else:
            print("this is odd number")

num = int(input("enter the number : "))
checkNumber(num)