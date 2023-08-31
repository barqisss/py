class person:
    def __init__(self, name):
       self.name = name 

    def say_hi(self):
        print("hello, my name is ", self.name)

person1 = person("cinta")
person1.say_hi()
