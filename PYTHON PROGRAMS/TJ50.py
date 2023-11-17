class father:
    def fishing(self):
        print("fishing in rivers")
    def chess (self):
        print("playing chess from father")
class mother:
    def cooking(self):
        print("cooking food")
    def chess(self):
        print("playing cjess from mother")
class son(mother,father):
    def ride(self):
        print("riding bicycle")
o=son()
o.ride()
o.fishing()
o.cooking()
o.chess()
