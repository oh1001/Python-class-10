class myclass:
    x = 5

p = myclass() #Object uusgeh
print(p.x)
print(type(p)) 

class person:
    fname = 'bold'
    lname = 'tumur'
    def hi(self):
        print('Hi I am', self.fname)
p1 = person()
p2 = person()
print(p1.fname)
p1.hi()
print(p2.fname)
p2.hi()


class person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def hi(self):
        print('Hi ?', 'I am', self.name)

numbers = [1,2, 3] # class list
names = ['a','z','c'] # class list

p = person('bold', 22)
p2 = person('baatar', 26)
print(p.name)
p.hi()
print(p2.name)
p2.hi()