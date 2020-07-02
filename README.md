# Practice with Ravelry
This is a collection of functions and Jupyter Notebooks that I am using for Python data analysis practice. 

## Prerequisites
- Have Python 3 installed
- Get Ravelry API key (Basic Auth works. See https://www.ravelry.com/api)

## Installation
1. Clone the repo (git clone https://github.com/acordonez/practice_with_ravelry.git)
2. Go to practice_with_ravelry directory
3. Create a ravelry_auth.csv document. This document contains *username,password* for your Ravelry project. (Csv files have been added to .gitignore)

## How to use
For running Jupyter Notebooks, see these instructions: https://jupyter.readthedocs.io/en/latest/running.html

To use the functions in rav_get for your own API requests, use `from rav_get import *` from within the same directory as rav_get.py.

## Acknowledgements
I spent some time using https://github.com/walkerkq/ravelRy to understand how to use the Ravelry API - it's a great tool for folks who are proficient in R. I have borrowed some concepts from that tool here.
