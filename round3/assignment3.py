# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:13:43 2021

@author: Vlad Dolghi
"""

import uuid
import csv
import pathlib
import json
import shutil

def create_car_dict():
    car_dict = {} 
    with open("input.csv") as car_file:
        car_reader = csv.reader(car_file)
        for row in car_reader:
            car_dict[str(uuid.uuid4())] = row[1:]
    return car_dict

def get_cars_by_hp(dataset, callback_condition):
    return {k:v for (k, v) in dataset.items() if callback_condition(int(v[2]))}

def get_cars_by_price(dataset, callback_condition):
    return {k:v for (k, v) in dataset.items() if callback_condition(float(v[3]))}

def write_json_data(data):
    slow_cars = get_cars_by_hp(data, lambda x: x < 120)
    fast_cars = get_cars_by_hp(data, lambda x: 120 <= x < 180)
    sport_cars = get_cars_by_hp(data, lambda x: x >= 180)
    cheap_cars = get_cars_by_price(data, lambda x: x < 1000)
    medium_priced_cars = get_cars_by_price(data, lambda x: 1000 <= x < 5000)
    expensive_cars = get_cars_by_price(data, lambda x: x >= 5000)
    
    output_path = pathlib.Path('./output_data')
    if not output_path.exists():
        output_path.mkdir()
    else:
        shutil.rmtree(str(output_path.resolve()))
        output_path.mkdir()
    
    json.dump(slow_cars, fp = open(output_path / 'slow_cars.json','w'))
    json.dump(fast_cars, fp = open(output_path / 'fast_cars.json','w'))
    json.dump(sport_cars, fp = open(output_path / 'sport_cars.json','w'))
    json.dump(cheap_cars, fp = open(output_path / 'cheap_cars.json','w'))
    json.dump(medium_priced_cars, fp = open(output_path / 'medium_cars.json','w'))
    json.dump(expensive_cars, fp = open(output_path / 'expensive_cars.json','w'))
    
if __name__ == '__main__':
    # Check it out, Lenny
    d = create_car_dict()
    write_json_data(d)
            