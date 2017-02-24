# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:15:58 2017
    Additional Requirment: Attrib contains 'Mexican'; City = Las Vegas
    
Prev/Basic Requirements:
    1. Categorie has restaurant' (if just 'food', would get Walgreens)
    2. # reviews it has is between 30-50
    3. It is located in the United STates+
    
@author: Janice
"""


import csv 

         
        
def read_and_write(reader, writer):
    _id = ['s6L6SdVYhPcOQEDmNIg1-g', 'McQsl_USMy6kfUz9J02Tdg' , 'QKCu3cKjMAOOZI7tEfv0zg']
    for row in reader:
        if row[6] == "": #ignore if no attrib
            continue
        attribs = eval(row[6]) #keep only if 'restaurant' is an attrib
        if row[7] != 'Las Vegas':
            continue
#        if 'Chinese' not in attribs or row[7] != 'Las Vegas' or len(attribs) != 2 or row[1] not in _id:
#            continue
        
        
        writer.writerow(row)
        
                     
      
#['neighborhood', 'business_id', 'hours', 'is_open', 'address', 'attributes', 'categories', 'city', 'review_count', 'name', 'longitude', 'state', 'stars', 'latitude', 'postal_code', 'type']
#[(0, 'neighborhood'), (1, 'business_id'), (2, 'hours'), (3, 'is_open'), 
#(4, 'address'), (5, 'attributes'), (6, 'categories'), (7, 'city'), 
#(8, 'review_count'), (9, 'name'), (10, 'longitude'), (11, 'state'), 
#(12, 'stars'), (13, 'latitude'), (14, 'postal_code'), (15, 'type')]
    
if __name__ == "__main__":
    print("START")
    fname = "filtered_business.csv"
    f = open(fname, 'r', encoding = 'utf8')
    
    ofname = "select_bus_vegas.csv"
    of = open(ofname, 'w', newline = '', encoding = 'utf8')
    
    writer = csv.writer(of)
    reader = csv.reader(f)
    
    for row in reader:
        writer.writerow(row)
        break
    
    read_and_write(reader, writer)
    of.close()
    f.close()
    print("END")
    
    
