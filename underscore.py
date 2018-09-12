class A(object):
    def __method(self):
        print "I'm a method in A"

    def method(self):
        self.__method()

a = A()
a.method()
print "data"
a._A__method()

class B(A):
    def __method(self, data):
        print "I'm a method in B",data
    def method(self):
        self.__method("inb")

b = B()
b.method()
# b._method()
b._B__method("mydata")
b.method()
b._A__method()
# b.method()
# print b.__method

class CrazyNumber(object):

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n - other

    def __sub__(self, other):
        return self.n * other

    def __str__(self):
        return str(self.n)

num = CrazyNumber(10)
print num           # 10
print num + 5       # 5
print num - 20      # 30
print num
print num - 100