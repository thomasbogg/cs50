import random


class Hat:

    # set a class variable for the randomiser to iterate over
    # here, the houses variable is meant to be left as it is
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    @classmethod
    # instead of referencing self, we reference class as 'cls'
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))


def main():
    Hat.sort('Harry')


if __name__ == '__main__':
    main()
