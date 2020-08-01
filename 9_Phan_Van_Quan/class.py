class natural()
    animal = "dong vat"
    plant = "thuc vat"
    def __init__(self, name ):
        self.name = name
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

print(animal.age)
animal.age = 40
buf = animal()

print(buf.age)

buf.age = 100
print(buf.age)
print(animal.age)