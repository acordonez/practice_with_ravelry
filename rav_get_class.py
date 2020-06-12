# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:54:59 2020

@author: Ana
"""


class ravelry_session():
    def __init__(auth_file):
        self.rav_session = requests.Session()
    
        with open(auth_file) as f:
            reader = csv.reader(f)
            rav_auth = list(reader)
        
        self.rav_session.auth = (rav_auth[0][0], rav_auth[0][1])
        
    
    
    def pattern_search(rav_query):
        # rav_query: dictionary of query items
        # rav_auth: list of ravelry name and password
        # returns the request response object
    
        rav_url = "https://api.ravelry.com/patterns/search.json"
        rav_params = rav_query

        rav_request = self.rav_session.get(url = rav_url, params = rav_params) 
    
        rav_request.raise_for_status()
    
        return rav_request