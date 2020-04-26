class Student(object):

    def __init__(self, something):
        print("Init called.")
        self.something = something

    def method(self):
        return self.something

my_object = Student('Jetty')
