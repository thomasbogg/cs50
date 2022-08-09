class Student:

    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError('Missing name')
        if house not in ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']:
            raise ValueError('Invalid house')

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house}'

    def charm(self):

        match self.patronus:
            case 'Stag':
                return 'horse emoji'
            case 'Otter':
                return 'caterpillar emoji'
            case 'Jack Russel terrier':
                return 'dog emoji'
            case _:
                return 'wand emoji'



def main():

    student = get_student()
    print('Expecto Patronum!')
    print(student.charm())


def get_student():
    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name, house, patronus)


if __name__ == '__main__':
    main()
