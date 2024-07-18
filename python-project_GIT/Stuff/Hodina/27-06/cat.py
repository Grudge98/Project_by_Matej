from animal import Animal


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)


    def make_sound(self):
        print("mnau mnau")