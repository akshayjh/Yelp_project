# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:31:59 2017
Filter business:
Basic Requirements:
    1. Categorie has restaurant' (if just 'food', would get Walgreens)
    2. # reviews it has is between 30-50
    3. It is located in the United STates

Check to see there is a distribution in the stars.
    
Additional Requirements for smaller dataset:
    
@author: Janice
"""

import csv 

         
        
def read_and_write(reader, writer):
    us_state = ['SC', 'IL', 'OH', 'NC', 'PA', 'VT', 'NV', 'NY', 'WI', 'AZ'] #already checked, only these states in dataset
    for row in reader:
        if row[6] == "": #ignore if no attrib
            continue
        attribs = eval(row[6]) #keep only if 'restaurant' is an attrib
        if 'Restaurants' not in attribs or int(row[8]) < 30 or int(row[8]) > 50 or row[11] not in us_state:
            continue
        writer.writerow(row)
        
                     
      
#['neighborhood', 'business_id', 'hours', 'is_open', 'address', 'attributes', 'categories', 'city', 'review_count', 'name', 'longitude', 'state', 'stars', 'latitude', 'postal_code', 'type']
#[(0, 'neighborhood'), (1, 'business_id'), (2, 'hours'), (3, 'is_open'), 
#(4, 'address'), (5, 'attributes'), (6, 'categories'), (7, 'city'), 
#(8, 'review_count'), (9, 'name'), (10, 'longitude'), (11, 'state'), 
#(12, 'stars'), (13, 'latitude'), (14, 'postal_code'), (15, 'type')]
    
if __name__ == "__main__":
    print("START")
    fname = "../dataset-examples-master/yelp_academic_dataset_business.csv"
    f = open(fname, 'r', encoding = 'utf8')
    
    ofname = "filtered_business.csv"
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
    
    f2 = "./dataset-examples-master/small_business.csv"
    
