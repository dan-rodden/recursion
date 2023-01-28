def a():
    print('a() was called')
    b()
    print('a() is returning')

def b():
    print('b() was called')
    c()
    print('b() is returning')

def c():
    print('c() was called')
    d()
    print('c() is returning')

def d():
    print('d() was called')
    print('d() is returning')

a()