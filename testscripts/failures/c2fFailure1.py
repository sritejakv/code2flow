"""
Dependency on initiliazation statements with in the same scope. Function call in quack is not identified
because its initialization statement is in init method.
"""


class Duck:
    def quack(self):
        print("Quack!")


class Mallard:
    def __init__(self):
        self.call = Duck()

    def quack(self):
        self.call.quack()


if __name__ == '__main__':
    o = Mallard()
    o.quack()
