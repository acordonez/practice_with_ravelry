# -*- coding: utf-8 -*-
"""
A small group of functions to make calling the Ravelry API easier

@author: Ana
"""
import requests
import csv

def ravelry_search(rav_query, rav_session):
    # rav_query: dictionary of query items
    # rav_auth: list of ravelry name and password
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/patterns/search.json"
    rav_params = rav_query

    rav_request = rav_session.get(url = rav_url, params = rav_params) 
    
    return rav_request

def ravelry_patterns(rav_ids, rav_session):
    # rav_ids: space delimited string of ids
    # rav_auth: list of ravelry name and password
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/patterns.json"
    rav_params = {'ids':rav_ids}

    rav_request = rav_session.get(url = rav_url, params = rav_params)
  
    return rav_request

def ravelry_get_ids(rav_result):
    # Returns the id string that can be used to query patterns
    # input: rav_result: output from ravelry_search
    # output: id_list: formatted string of ids
    
    rav_json = rav_result.json()
    
    id_list = ''
    
    for key in range(len(rav_json['patterns'])):
        id_list += (str(rav_json['patterns'][key]['id']) + ' ')
        
    # remove the last white space
    return id_list[:-1]

def ravelry_load_auth(auth_file):
    # loads your ravelry api authentication info from csv
    # and creates and returns a session object
    
    rav_session = requests.Session()
    
    with open(auth_file) as f:
        reader = csv.reader(f)
        rav_auth = list(reader)
        
    rav_session.auth = (rav_auth[0][0], rav_auth[0][1])
    
    return rav_session