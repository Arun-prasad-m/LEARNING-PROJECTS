class Grandfather():
    def ownhouse(self):
        print("Grandpa house")
class Father(Grandfather):
    def ownbike(self):
        print("father's bike")
class son(Father):
    def ownbook(self):
        print("son have a book")
o=son()
o.ownhouse()
o.ownbike()
o.ownbook()