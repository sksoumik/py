# we can add super() function that will make the child class inherit all the methods and properties from its parent.


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)