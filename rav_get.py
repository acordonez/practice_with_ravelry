# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:11:32 2020

@author: Ana
"""
import requests
from requests.auth import HTTPBasicAuth
import csv

def ravelry_search(rav_query, rav_auth):
    # rav_query: dictionary of query items
    # rav_auth: list of ravelry name and password
    
    rav_url = "https://api.ravelry.com/patterns/search.json"
    rav_params = rav_query

    rav_request = requests.get(url = rav_url, params = rav_params, auth=HTTPBasicAuth(rav_auth[0][0], rav_auth[0][1])) 
    
    return rav_request.json()

def ravelry_patterns(rav_ids, rav_auth):
    # rav_ids: space delimited string of ids
    # rav_auth: list of ravelry name and password
    # returns dictionary of patterns
    
    rav_url = "https://api.ravelry.com/patterns.json"
    rav_params = {'ids':rav_ids}

    rav_request = requests.get(url = rav_url, params = rav_params, auth=HTTPBasicAuth(rav_auth[0][0], rav_auth[0][1]))
  
    return rav_request.json()

def ravelry_get_ids(rav_result):
    # Returns the id string that can be used to query patterns
    # input: rav_result: output from ravelry_search
    # output: id_list: formatted string of ids
    
    id_list = ''
    
    for key in range(len(rav_json['patterns'])):
        id_list += (str(rav_json['patterns'][key]['id']) + ' ')
        
    return id_list[:-1]

def ravelry_load_auth(auth_file):
    # loads your ravelry api authentication info from csv
    
    with open(auth_file) as f:
        reader = csv.reader(f)
        rav_auth = list(reader)
        
    return rav_auth