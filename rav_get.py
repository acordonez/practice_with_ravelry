# -*- coding: utf-8 -*-
"""
A small group of functions to make calling the Ravelry API easier

@author: Ana
"""
import requests
import csv

def ravelry_pattern_search(rav_query, rav_session):
    # rav_query: dictionary of query items
    # rav_auth: list of ravelry name and password
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/patterns/search.json"
    rav_params = rav_query

    rav_request = rav_session.get(url = rav_url, params = rav_params) 
    
    rav_request.raise_for_status()
    
    return rav_request

def ravelry_project_search(rav_query, rav_session):
    # rav_query: dictionary of query items
    # rav_session: requests session object
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/projects/search.json"
    rav_params = rav_query

    rav_request = rav_session.get(url = rav_url, params = rav_params) 
    
    rav_request.raise_for_status()
    
    return rav_request

def ravelry_designer(designer_id, rav_session):
    # designer_id: string, the designer id number
    # rav_session: requests session object
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/designers/"+str(designer_id)+".json"

    rav_request = rav_session.get(url = rav_url)
    
    rav_request.raise_for_status()
    
    return rav_request

def ravelry_patterns(rav_result, rav_session):
    # rav_ids: space delimited string of ids
    # rav_session: requests session object
    # returns the request response object
    
    rav_url = "https://api.ravelry.com/patterns.json"
    rav_ids = ravelry_get_ids(rav_result)
    rav_params = {'ids':rav_ids}

    rav_request = rav_session.get(url = rav_url, params = rav_params)
  
    rav_request.raise_for_status()
    
    return rav_request

def ravelry_get_ids(rav_result):
    # Returns the id string that can be used to query patterns
    # rav_result: output from ravelry_search
    # id_list: formatted string of ids
    
    rav_json = rav_result.json()
    id_list = ''
    
    for key in range(len(rav_json['patterns'])):
        id_list += (str(rav_json['patterns'][key]['id']) + ' ')
        
    # remove the last white space
    return id_list[:-1]

def ravelry_load_auth(auth_file):
    # loads your ravelry api authentication info from csv
    # and creates and returns a session object
    # auth_file: string, csv file with username,password
    
    rav_session = requests.Session()
    
    with open(auth_file) as f:
        reader = csv.reader(f)
        rav_auth = list(reader)
        
    rav_session.auth = (rav_auth[0][0], rav_auth[0][1])
    
    return rav_session