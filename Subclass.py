# Python example to check if a class is
# subclass of another

class Base(object):
    pass  # Empty Class


class Derived(Base):
    pass  # Empty Class


# Driver Code
print("issubclass(Derived, Base )")
print(issubclass(Derived, Base))
print("issubclass(Base, Derived )")
print(issubclass(Base, Derived))

d = Derived()
d.data = "12"
d.name = "Sudhakar"
b = Base()

# b is not an instance of Derived
print("isinstance(b, Derived)")
print(isinstance(b, Derived))

# But d is an instance of Base
print("isinstance(d, Base)")
print(isinstance(d, Base))

print d.data
print d.name