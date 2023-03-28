#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:19:23 2022

@author: Nicolle Mathieu
"""
import os
import pandas as pd
import requests
import json
from geopy.geocoders import Nominatim
from credentials import API_KEY

def get_gps_coordinates(address):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    if location is not None:
        return location.latitude, location.longitude
    else:
        return None

def get_nearest_adress(lat,long):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        address = data["results"][0]["formatted_address"]
        return address
    else:
        return None

def define_str_point(lat_value,long_value):
    point = f"{lat_value},{long_value}"
    return point

def call_api(start_point, end_point):
    key=API_KEY
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_point}&destination={end_point}&mode=bicycling&key={key}"
    response = requests.get(url)
    data = response.json()
    path_steps = data["routes"][0]["legs"][0]["steps"]
    list_coor = list()
    for i in range(len(path_steps)):
        if i == 0:
            list_coor.append([path_steps[i]["start_location"]["lng"],path_steps[i]["start_location"]["lat"]])
        list_coor.append([path_steps[i]["end_location"]["lng"],path_steps[i]["end_location"]["lat"]])
    output_json = {"type": "Feature","geometry": {"type": "LineString","coordinates": list_coor}}
    print(output_json)


def get_traject(adress_start,adress_end):
    start_lat,start_long = get_gps_coordinates(address_start)
    end_lat,end_long = get_gps_coordinates(address_end)
    start_point = define_str_point(start_lat,start_long)
    end_point = define_str_point(end_lat,end_long)
    call_api(start_point,end_point)



if __name__ == '__main__':
    address_start = "39 Cours Emile Zola 69100 Villeurbanne"
    address_end = "10 rue de Montbrillant 69003 Lyon"
    # Main function
    get_traject(address_start,address_end)
