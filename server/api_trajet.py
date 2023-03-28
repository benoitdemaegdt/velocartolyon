#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:19:23 2022

@author: Nicolle Mathieu
"""
import os
import pandas as pd
import requests
from credentials import API_KEY


def call_api(start_point, end_point):
    
    key=API_KEY
    start_coordinates = "37.421999,-122.084057"  # Replace with your starting point coordinates
    end_coordinates = "37.7749,-122.4194"  # Replace with your ending point coordinates
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_coordinates}&destination={end_coordinates}&key={key}"
    response = requests.get(url)
    data = response.json()
    print(data)
    """
    if data['status'] == 'OK':
        for route in data['routes']:
            for leg in route['legs']:
                print(f"Distance: {leg['distance']['text']}")
                print(f"Duration: {leg['duration']['text']}")
                print("Steps:")
                for step in leg['steps']:
                    print(f"{step['html_instructions']} for {step['distance']['text']} ({step['duration']['text']})")
    else:
        print(f"Error: {data['status']}")
    """
        


if __name__ == '__main__':
    # Main function
    call_api(1,2)
    
    

