print("welocme to scope tutorials")

x = 5

def change():
    global x
    x = 10

change()
print(x)
