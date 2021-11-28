 # Author:LindomHui
 # coding=---UTF-8---

for i in range(1, 10, 2):
    print(('* '* i).center(30))

for i in range(7, 0, -2):
    print(('* ' * i ).center(30))

def startower(x):
    for i in range(1, 2*x, 2):
        print(('* '* i ).center(4*x))
startower(50)
def startower(x):
    for i in range(2*x-3, 0, -2):
        print(('* '* i ).center(4*x))
startower(50)

