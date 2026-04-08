"""def re_num(num):
    if num > 10:   # correct base case
        return
    print(num)
    re_num(num + 1)

re_num(1)


# printing name 5 time 
def print_name(name,count):
    if count == 5:
        return
    print(name)
    print_name(name,count + 1)
    
print_name("kalpesh",0)

count = 0
def count_name(name):
    global count
    if count == 5:
        return
    print(name)
    count += 1
    count_name(name)

count_name('kal')

def n_to_1(num):
    if  num < 1:
        return 
    print(num)
    n_to_1(num-1)
n_to_1(10)"""

count = 0
def fun():
    global count
    if count == 4:
        return
    print("anirudha")
    count += 1
    fun()
fun()

# print x to n time 
def xToN(x,n):
    if n == 0:
        return
    print(x)
    xToN(x,n-1)
xToN('kalpesh',5)

# prinbt 1 to 10

def oneToTen(el,v):
    if el >= v:
        return

    print(el)
    oneToTen(el+1,v)
oneToTen(1,10)


# sum of first n number
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))
   

def summ(sum,x,n):
    if x > n:
        print(sum)
        return
    summ(sum+x,x+1,n)
summ(0,1,5)


    
 
    