"""
All the strings are replaced by empty characters. The dictionary in the call is made useless because of this feature.
It is modified as x = {'': Cat(), '': Dog()}.
"""


class Dog:
    def bark(self):
        print("Bow bow!")


class Cat:
    def bark(self):
        print("Meow meow!")


class Animal:
    def call(self):
        x = {'c': Cat(), 'd': Dog()}
        x['c']()


if __name__ == '__main__':
    x = Animal()
    x.call()