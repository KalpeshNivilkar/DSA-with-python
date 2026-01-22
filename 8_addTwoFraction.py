def addTwoFraction():
    a = int(input("enter numerator 1: "))
    b = int(input("enter denometor 1: "))
    c = int(input("enter numerator 2: "))
    d = int(input("enter denometor 2: "))

    numerator = (a * d) + (b * c)
    denometor = (b * d)

    # result1 = numerator / denometor
    result2 = ("the result = {}/{}".format(numerator,denometor))
    print(result2)
addTwoFraction()


def addFraction():
    a = int(input("enter the numerator1 :"))
    b = int(input("enter the denometor1 :"))
    c = int(input("enter the numerator2 :"))
    d = int(input("enter the denometer2 :"))

    numerator = (a*d) + (c*b)
    denometor = (b*d)

    result = "the result = {}/{}".format(numerator,denometor)
    print(result)