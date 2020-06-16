# -*- coding: utf-8 -*-
"""
The ravelry_session class is a collection of api request
functions for more easily querying the Ravelry.com data. 

For queries, you can use the same keywords and search
terms that are used on the Ravelry.com search pages

@author: Ana
"""
import requests
import csv

class ravelry_session():
    def __init__(self, auth_csv):
        """ 
        Creating a ravelry session helps you query Ravelry data
        quickly and easily, without building a new http request
        every time.
        
        Parameters:
        auth_csv:   string. Path to a csv containing your 
                    ravelry API username,password
        """
        
        self.rav_session = requests.Session()
    
        with open(auth_csv) as f:
            reader = csv.reader(f)
            rav_auth = list(reader)
        
        self.rav_session.auth = (rav_auth[0][0], rav_auth[0][1])
        
    def ravelry_request(self, rav_url, rav_params):
        """ 
        Used by other functions to make http requests
        Parameters: 
            rav_url: string
            rav_params: string
        Returns:
            rav_request: response object
        """
        
        rav_request = self.rav_session.get(url = rav_url, params = rav_params)
        rav_request.raise_for_status()
        
        return rav_request
        
    def pattern_search(self, rav_query):
        """ 
        Use this function to return pattern search results (Pattern list
        result from Ravelry API)
        Parameters:
            rav_query: dictionary. e.g. {'query': 'v-neck', ...
                                         'pc': 'cardigan', 'page': '1'}
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/patterns/search.json"

        return self.ravelry_request(rav_url, rav_query)
    
    def yarn_search(self, rav_query):
        """ 
        Use this function to return yarn search results (Yarn list
        result from Ravelry API)
        Parameters:
            rav_query: dictionary. e.g. {'query': 'wool', 'page': '1'}
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/yarns/search.json"

        return self.ravelry_request(rav_url, rav_query)
    
    def project_search(self, rav_query):
        """ 
        Use this function to return project search results (Project list
        result from Ravelry API)
        Parameters:
            rav_query: dictionary. e.g. {'query': 'v-neck', ...
                                         'pc': 'cardigan', 'page': '1'}
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/projects/search.json"
        
        return self.ravelry_request(rav_url, rav_query)
    
    def get_patterns(self, rav_query):
        """ 
        Use this function to return the full pattern details
        for the results from a pattern query
        Parameters:
            rav_query: dictionary. e.g. {'query': 'v-neck', ...
                                         'pc': 'cardigan', 'page': '1'}
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/patterns.json"
        rav_ids = self.get_ids(self.pattern_search(rav_query).json()['patterns'])
        rav_params = {'ids':rav_ids}

        return self.ravelry_request(rav_url, rav_params)
    
    def get_yarns(self, rav_query):
        """ 
        Use this function to return the full pattern details
        for the results from a pattern query
        Parameters:
            rav_query: dictionary. e.g. {'query': 'angora', ...
                                         'sort': 'best', 'page': '1'}
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/yarns.json"
        rav_ids = self.get_ids(self.yarn_search(rav_query).json()['yarns'])
        rav_params = {'ids':rav_ids}

        return self.ravelry_request(rav_url, rav_params)
    
    def get_designer(self, designer_id):
        """ 
        Use this function to return full details for a specific designer
        Parameters:
            designer_id: string
        Returns: 
            rav_request: http response object. Use rav_request.json()
                        to access data json
        """
    
        rav_url = "https://api.ravelry.com/designers/"+str(designer_id)+".json"
        
        return self.ravelry_request(rav_url, '')
    
    def get_ids(self, rav_json):
        """
        Pulls a list of ids from a list result to help with querying
        the full result. Used by other functions in ravelry_session
        Parameters:
            rav_json: the json portion of a response object, without the 
                      paginator. e.g. rav_request.json()['patterns']
        Returns:
            id_list: a formatted list of ids
        """
    
        id_list = ''
    
        for key in range(len(rav_json)):
            id_list += (str(rav_json[key]['id']) + ' ')
        
        # remove the last white space
        return id_list[:-1]
    
    def get_pattern_categories(self):
        """ 
        Returns the full list of all Ravelry pattern categories
        Use the .json() method to view the results
        """
    
        rav_url = "https://api.ravelry.com/pattern_categories/list.json"
    
        return self.ravelry_request(rav_url, '')
    
    def get_pattern_attributes(self):
        """ 
        Returns the full list of all Ravelry pattern attributes
        Use the .json() method to view the results
        """
    
        rav_url = "https://api.ravelry.com/pattern_attributes/groups.json"
    
        return self.ravelry_request(rav_url, '')