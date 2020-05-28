'''
Created on Dec 1, 2019

@author: jackyi
'''
import os
import requests

print(os.getcwd())
r=requests.get("http://www.google.com")
print(r.url)
print(r.encoding);
print(r.text);
