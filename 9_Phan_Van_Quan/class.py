class animal():
    name = ''
    age = 0
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
    def show(self):
        print('my name is ', self.name)
    def ages(self):
        print('my age is', self.age)
    def run(self):
        print('Animal is running')
    def go(self):
        print('Animal is going')

class dog(animal):
    def go(self):
        print('Dog is going')
myanimal = animal('lucky')
myanimal.ages()
myanimal.show()
myanimal.run()
myanimal.go()

mydog = dog('lucky')
mydog.show()
mydog.run()
mydog.go()