# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print('flying')
#
# class Penguin(Bird):
#     pass
#
# p = Penguin('sara')
# p.fly()

class Bird():
    def fly(self):
        print('flying')

class Duck(Bird):
    def fly(self):
        print('fast flying')

def fli_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fli_in_the_sky(b)
fli_in_the_sky(d)

