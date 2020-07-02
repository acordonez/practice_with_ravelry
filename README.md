# Practice with Ravelry
This is a collection of functions and Jupyter Notebooks that I am using for Python data analysis practice. 

## Prerequisites
- Have Python 3 installed
- Install the following packages: requests, csv, numpy, datetime, matplotlib, scipy (only requests and csv are needed to use the rav_get functions or ravelry_session class)
- Get Ravelry API key (Basic Auth is ok. See https://www.ravelry.com/api)

## Installation
1. Clone the repo (git clone https://github.com/acordonez/practice_with_ravelry.git)
2. Go to practice_with_ravelry directory
3. Create a ravelry_auth.csv document. This document contains *username,password* for your Ravelry project. (Csv files have been added to .gitignore)

## How to use
For running Jupyter Notebooks, see these instructions: https://jupyter.readthedocs.io/en/latest/running.html

To use the functions in rav_get for your own API requests, use `from rav_get import *` from within the same directory as rav_get.py.

### Examples for ravelry_session

Initialize a Ravelry session:  
`from ravelry_session import ravelry_session`  
`s = ravelry_session('ravelry_auth.csv')`
  
Make a query for certain types of patterns, sorted by most relevant:  
`my_query = {'query': 'cables', 'pc': 'hat', 'weight': 'dk', 'sort': 'best'}`  
`results = s.pattern_search(my_query)`  
You can use any of the keywords used in the pattern search on Ravelry.com (look at the keywords in the URL for a search).  

This returns an http request object (more info at https://requests.readthedocs.io/en/master/). To view the json data use:  
`results.json()`

## Acknowledgements
I spent some time using https://github.com/walkerkq/ravelRy to understand how to use the Ravelry API - it's a great tool for folks who are proficient in R. I have borrowed some concepts from that tool here.
