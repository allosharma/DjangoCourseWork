a = 10

def use_global():
    global a #using global uses the global variable
    a += 5
    print("Inside function, a =", a)

use_global()