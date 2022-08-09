# classes allow you to invent your own data-types in python
# they are blueprints for pieces of data objects


class Student:
    ...


def main():
    student = get_student()
    print(f'{student.name} from {student.house}')


def get_student():
    student = Student()
    # every time we call a class, we are creating an object of that class
    student.name = input('Name: ')
    student.house = input('House: ')
    # .name and .house work even with the Student class being empty
    # they are attributes of the Student class, aka Instance Variables
    return student


if __name__ == '__main__':
    main()
