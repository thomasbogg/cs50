class Student:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'

    # this class method is called before the init, to retrieve the user input
    # it then returns a call to the init method of the class itself
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house)


def main():
    student = Student.get() # class is called for the first time using the class method get()
    print(student)


if __name__ == '__main__':
    main()
