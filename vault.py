# OPERATOR OVERLOADING

class Vault:

    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'

    # in order to add two instances
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# Question: how would you combine the contents of these two vaults?
"""
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print('Total:', total)
"""
# Wouldn't it be better if we could just do something like this:
# total = potter + weasley

total = potter.__add__(weasley)
print(total)
