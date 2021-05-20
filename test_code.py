class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def get_name(self):
        return self.name

    def get_designation(self):
        return self.designation

    def __str__(self):
        return f"Name: {self.name}, Position: {self.designation}"


if __name__ == "__main__":
    emp_1 = Employee("Jeff Bezos", "CEO")
    print(emp_1)
