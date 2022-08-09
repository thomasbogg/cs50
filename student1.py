class Student:

    def __init__(self, name, house):

        self.name = name
        self.house = house
        '''leaving self.house and self.name variables as are, instead of defining
        them as self._house and self._name like in the getter and setter functions,
        makes sure python calls those functions whenever someone tries to
        set these variables as part of the initialising class call'''


    def __str__(self):
        return f'{self.name} from {self.house}'


    # Getter - function in a class that gets a value
    @property
    def house(self):
        return self._house


    # Setter - function in a class that sets a value
    '''use a function to set an instance variable to prevent user/programmer
    from circumventing any specific property requirements of the variable'''
    @house.setter
    # this setter will get called anytime .house is accessed
    def house(self, house):
        '''whenever dot notation is now used to set the value of this instance
        variable, the value will be chacked against the following condition'''
        if house not in ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']:
            raise ValueError('Invalid house')

        self._house = house
        # use an underscore in the variable to distinguish it from the function


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')

        self._name = name


def main():
    student = get_student()
    # using a setter function to defend against variable setting of this sort:
    student.house = 'Number Four, Privet Drive'
    print(student)


def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name, house)


if __name__ == '__main__':
    main()
