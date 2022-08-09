# OOP encourages you to encapture within a certain class all functionality
# related to that class
class Student:

    # the 'dunder_score' init method initialises the contents of an object from a class
    # a method is just a function inside of a class
    def __init__(self, name, house):

        if not name:                            # i.e. if name is blank
            raise ValueError('Missing name')    # we can raise our own error

        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')

        self.name = name
        self.house = house


    # function to set default object print call
    # can set it to make the print call in the main() below redundant
    def __str__(self):
        return f'{self.name} from {self.house}'


def main():
    student = get_student()
    # next line made redundant by the __str__() method in the Student class
    # print(f'{student.name} from {student.house}')
    print(student)


def get_student():
    name = input('Name: ')
    house = input('House: ')
    # now we are passing the input to the class and defining Attributes in the class
    # the next line is what is known as a Constructor Call
    return Student(name, house)


if __name__ == '__main__':
    main()
