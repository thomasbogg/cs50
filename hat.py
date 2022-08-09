'''Creating a sorting hat program using a class called Hat with method
that accesses the random module to randomly give a given name a house'''

import random


class Hat:

    def __init__(self):
        self.houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    def sort(self, name):
        print(name, 'is in', random.choice(self.houses))


def main():
    hat = Hat()
    hat.sort('Harry')


if __name__ == '__main__':
    main()

"""
When to use a class? a
When trying to represent some real-world entity. Like a student, a worker, etc.
Categories of which there are multiple instances.

Using a class in this instance to define a sorting hat does not quite match
the singleton status of the sorting hat in the world of harry potter.
Instantiating the class here means that multiple sorting hats could be
activated, which is contrary to the singleton staues of the hat.

For the hat, using a @classmethod would be the most appropriate.

see hat2.py for the changes applied by this decision
"""
