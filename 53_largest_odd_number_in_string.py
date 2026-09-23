# find the largest odd number in string 
def larget_odd_num(num):
    n = len(num)
    for i in range(n-1,-1,-1):
        if int(num[i]) % 2 == 1:
            return num[0:i+1]
    return ""

num = "3458"
print(larget_odd_num(num))


# find the larget odd number in the string 
def largest_odd_num(num):
    n = len(num)
    for i in range(n-1,-1,-1):
        if int(num[i]) % 2 == 1:
            return num[0:i+1]
    return ""

num = "89749272"
print(larget_odd_num(num))

def large_odd_num(num):
    n = len(num)
    for i in range(n-1,-1,-1):
        if int(num[i]) % 2 == 1:
            return num[0:i+1]
    return ""

num = "89749272"
print(large_odd_num(num))


def lar_odd_num(num):
    n = len(num)
    for i in range(n-1,-1,-1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return " "
num = "9842398"
print(lar_odd_num(num))
