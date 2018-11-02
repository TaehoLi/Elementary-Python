def calc(op,a,b):
    op(a,b)

def add(a,b):
    print(a+b)

def multi(a,b):
    print(a*b)

calc(add,1,2)
calc(multi,3,4)
