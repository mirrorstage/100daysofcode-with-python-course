#!/usr/bin/env python3

import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeepString = cars['Jeep'][0] + ', ' + cars['Jeep'][1] + ', ' + cars['Jeep'][2] + ', ' + cars['Jeep'][3]
    return jeepString


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    firstModelList = []
    for k, v in cars.items():
        firstModelList.append(v[0])
    return firstModelList


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    modelMatches = []
    grep = grep.lower()
    carsRegex = re.compile(grep)
    for each in cars.values():
        for car in each:
            mo = carsRegex.search(car.lower())
            if mo == None:
                continue
            else:
                modelMatches.append(car)
    return sorted(modelMatches)


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    sortedCars = cars
    for k, v in sortedCars.items():
        sortedCars[k] = sorted(v)
    print(sortedCars)
    return sortedCars

get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models()
sort_car_models()