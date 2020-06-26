"""
Incorrect regular expression for generateNewOBjectAssignedPattern. '\w' should be replaced by '\w*'.
variable names should be compared rather than comparing them after including the namespaces
"""


class Foo:
    def __init__(self, a):
        self.a = a

    def function_one(self):
        pass


if __name__ == '__main__':
    obj = Foo("")
    obj.function_one()
