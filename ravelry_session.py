# -*- coding: utf-8 -*-
"""
The ravelry_session class collects the api request
functions for querying the ravelry.com data. 

@author: Ana
"""
import requests
import csv

class ravelry_session():
    def __init__(self):
        # initiate a ravelry session based on credentials in 
        # local 'ravelry_auth.csv' file (containing username,password)
        
        self.rav_session = requests.Session()
    
        with open('ravelry_auth.csv') as f:
            reader = csv.reader(f)
            rav_auth = list(reader)
        
        self.rav_session.auth = (rav_auth[0][0], rav_auth[0][1])
        
    def ravelry_request(self, rav_url, rav_params):
        # makes api request with given url and parameters
        
        rav_request = self.rav_session.get(url = rav_url, params = rav_params)
        rav_request.raise_for_status()
        
        return rav_request
        
    def pattern_search(self, rav_query):
        # rav_query: dictionary of query items
        # returns the request response object
    
        rav_url = "https://api.ravelry.com/patterns/search.json"

        return self.ravelry_request(rav_url, rav_query)
    
    def project_search(self, rav_query):
        # rav_query: dictionary of query items
        # returns the request response object
    
        rav_url = "https://api.ravelry.com/projects/search.json"
        
        return self.ravelry_request(rav_url, rav_query)
    
    def get_patterns(self, rav_query):
        # rav_ids: space delimited string of ids
        # returns the request response object
    
        rav_url = "https://api.ravelry.com/patterns.json"
        rav_ids = self.get_ids(self.pattern_search(rav_query))
        rav_params = {'ids':rav_ids}

        return self.ravelry_request(rav_url, rav_params)
    
    def get_designer(self, designer_id):
        # designer_id: string, the designer id number
        # returns the request response object
    
        rav_url = "https://api.ravelry.com/designers/"+str(designer_id)+".json"
        
        return self.ravelry_request(rav_url, '')
    
    def get_ids(self, rav_result):
         # Returns the id string that can be used to query patterns
         # id_list: formatted string of ids
    
        rav_json = rav_result.json()
        id_list = ''
    
        for key in range(len(rav_json['patterns'])):
            id_list += (str(rav_json['patterns'][key]['id']) + ' ')
        
        # remove the last white space
        return id_list[:-1]
    
    def get_pattern_categories(self):
        # returns full list of all the possible pattern categories
    
        rav_url = "https://api.ravelry.com/pattern_categories/list.json"
    
        return self.ravelry_request(rav_url, '')
    
    def get_pattern_attributes(self):
        # returns full list of of all the possible pattern attributes
    
        rav_url = "https://api.ravelry.com/pattern_attributes/groups.json"
    
        return self.ravelry_request(rav_url, '')