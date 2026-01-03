# given number check is positive,negative,odd,even,zero

def checkNumber(n):
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

(checkNumber(28))