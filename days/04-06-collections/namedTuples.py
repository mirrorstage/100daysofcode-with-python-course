from collections import namedtuple
import pprint

Bandmember = namedtuple('Bandmember', 'name instrument isSoloist')


bandmember01 = Bandmember(name = 'Dizzy Gillespie', instrument = 'trumpet', isSoloist = False)
bandmember02 = Bandmember(name = 'Charlie Parker', instrument = 'alto saxaphone', isSoloist = False)
bandmember03 = Bandmember(name = 'John Lewis', instrument = 'piano', isSoloist = False)
bandmember04 = Bandmember(name = 'Al McKibbon', instrument = 'bass', isSoloist = False)
bandmember05 = Bandmember(name = 'Joe Harris', instrument = 'drums', isSoloist = False)

Quartet = (bandmember01, bandmember02, bandmember03, bandmember04, bandmember05)

# pprint.pprint('The soloists are: ')

for Bandmember in Quartet:
    if 
    elif Bandmember.isSoloist == True:
        pprint.pprint(Bandmember.name + ' is a soloist.')
    elif Bandmember.isSoloist == False:
            pprint.pprint(Bandmember.name + ' is not a soloist.')
    else:
        pprint.pprint('There are no soloists in the Quartet.')
