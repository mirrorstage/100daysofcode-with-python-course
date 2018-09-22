#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:58:03 2018

@author: lacroix
"""
from collections import defaultdict, namedtuple

# testDict = {k:v for k, v in mydefaultdict.items() if v['records_available'] == True }

anotherDefaultDict = defaultdict(dict)
anotherDefaultDict['James Cameron']['movie'] = 'Escape From New York'
anotherDefaultDict['James Cameron']['year'] = int(1981)
anotherDefaultDict['James Cameron']['score'] = float(7.2)
anotherDefaultDict['James Cameron']['color'] = True
anotherDefaultDict['Kathryn Bigelow']['movie'] = 'Zero Dark Thirty'
anotherDefaultDict['Kathryn Bigelow']['year'] = int(2012)
anotherDefaultDict['Kathryn Bigelow']['score'] = float(7.4)
anotherDefaultDict['Kathryn Bigelow']['color'] = True
anotherDefaultDict['Jordan Peele']['movie'] = 'Get Out'
anotherDefaultDict['Jordan Peele']['year'] = int(2017)
anotherDefaultDict['Jordan Peele']['score'] = float(7.7)
anotherDefaultDict['Jordan Peele']['color'] = True
anotherDefaultDict['RZA']['movie'] = 'The Man with the Iron Fists'
anotherDefaultDict['RZA']['year'] = int(2012)
anotherDefaultDict['RZA']['score'] = float(5.4)
anotherDefaultDict['RZA']['color'] = True
anotherDefaultDict['Amy Heckerling']['movie'] = 'Clueless'
anotherDefaultDict['Amy Heckerling']['year'] = int(1995)
anotherDefaultDict['Amy Heckerling']['score'] = float(6.8)
anotherDefaultDict['Amy Heckerling']['color'] = True
anotherDefaultDict['Alan Smithee']['movie'] = 'The One True Thing'
anotherDefaultDict['Alan Smithee']['year'] = int(1950)
anotherDefaultDict['Alan Smithee']['score'] = float(3.2)
anotherDefaultDict['Alan Smithee']['color'] = False


Movie2 = namedtuple('movie2', ('year score color'))

thirdDefaultDict = defaultdict(dict)
