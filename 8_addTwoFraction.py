def addTwoFraction():
    a = int(input("enter numerator 1: "))
    b = int(input("enter denometor 1: "))
    c = int(input("enter numerator 2: "))
    d = int(input("enter denometor 2: "))

    numerator = (a * d) + (b * c)
    denometor = (b * d)

    result = numerator / denometor
    print(result)
addTwoFraction()