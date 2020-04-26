class Person:
    def __init__(self, name='Unknown', age=0):
        self.name = name
        self.age = age

    def display_data(self):
        print(self.name)
        print(self.age)
