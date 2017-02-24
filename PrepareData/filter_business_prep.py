
"""
Created on Tue Feb 21 20:33:57 2017

@author: Janice
"""

import csv


def get_attrib(reader, d, x):
    for row in reader:
        try:
            if reader.line_num == 1:
                print(list(enumerate(row)))
                continue
            x +=1
            if x %2000 ==0 :
                print(x)
            if row[6] != "":
                for i in eval(row[6]):
                    if i not in d.keys():
                        d[i] = 1
                    else:
                        d[i] +=1
        except:
            print(reader.line_num, row[9])
        
def test_attrib_combos(reader):
    f = dict()
    r = dict()
    d = dict()
    for row in reader:
        if row[6] != "":
            attrib = eval(row[6])
            if 'Food' in attrib and 'Restaurants' not in attrib:
                if row[9] not in f:
                    f[row[9]] = 1
                else:
                    f[row[9]] +=1
            elif 'Food' not in attrib and 'Restaurants'in attrib:
                if row[9] not in r:
                    r[row[9]] = 1
                else:
                    r[row[9]] +=1
            elif 'Food' in attrib and 'Restaurants' in attrib:
                if row[9] not in d:
                    d[row[9]] = 1
                else:
                    d[row[9]] +=1  
    print("food w/o restaurants")
    print_dict(f)
    print("restaurants w/o food")
    print_dict(r)
    print("food and restaurants")
    print_dict(d) 
    
def store_state_abbrev():
    fname = "state_abbrev.txt"
    f = open(fname, 'r')
    state_list = f.read().splitlines()
    f.close()
    return state_list

def get_state(reader, d, x):
    for row in reader:
        try:
            if reader.line_num == 1:
                print(list(enumerate(row)))
                continue
            x +=1
            if x %2000 ==0 :
                print(x)
            info = row[11]
            if info not in d.keys():
                d[info] = 1
            else:
                d[info] +=1
        except:
            print(reader.line_num, row[9])

def eval_state(d):            
    state_list = store_state_abbrev()
    us_state = []
    not_us_state = []
    for i in d.keys():
        if i in state_list:
            us_state.append(i)
        else:
            not_us_state.append(i)
    print("us_state", us_state)
    print("not_us_state", not_us_state)

def get_general(reader, d, x, i):
    for row in reader:
        try:
            if reader.line_num == 1:
                print(list(enumerate(row)))
                continue
            x +=1
            if x %2000 ==0 :
                print(x)
            info = row[i]
            if info not in d.keys():
                d[info] = 1
            else:
                d[info] +=1
        except:
            print(reader.line_num, row[9])
    print(x)       

      
def print_dict(d):
    d = sorted(d.items(),key = lambda x: (x[1], x[0]), reverse = True)
    for i in d[:10]:
        print(i)
    print("=")
    for i in d[-10:]:
        print(i)  
    print("===========")
    return


            
        
def test_combos(reader):
    f = dict()
    r = dict()
    d = dict()
    for row in reader:
        if row[6] != "":
            attrib = eval(row[6])
            if 'Food' in attrib and 'Restaurants' not in attrib:
                if row[9] not in f:
                    f[row[9]] = 1
                else:
                    f[row[9]] +=1
            elif 'Food' not in attrib and 'Restaurants'in attrib:
                if row[9] not in r:
                    r[row[9]] = 1
                else:
                    r[row[9]] +=1
            elif 'Food' in attrib and 'Restaurants' in attrib:
                if row[9] not in d:
                    d[row[9]] = 1
                else:
                    d[row[9]] +=1  
    print("food w/o restaurants------")
    print_dict(f)
    print("restaurants w/o food------")
    print_dict(r)
    print("food and restaurants------")
    print_dict(d) 
    f = set(f.keys())
    r = set(r.keys())
    d = set(d.keys())
    fr = [f,r]
    fd = [f,d]
    rd = [r,d]
    frd = [f,r,d]

    oall = set.intersection(*frd)
    print("frd: -------")
    print(oall)  
    
    print("fr: -------")
    print(set.intersection(*fr)-oall)
    print("fd: -------")
    print(set.intersection(*fd)-oall)
    print("rd: -------")
    print(set.intersection(*rd)-oall)
  
        
      
#['neighborhood', 'business_id', 'hours', 'is_open', 'address', 'attributes', 'categories', 'city', 'review_count', 'name', 'longitude', 'state', 'stars', 'latitude', 'postal_code', 'type']
#[(0, 'neighborhood'), (1, 'business_id'), (2, 'hours'), (3, 'is_open'), 
#(4, 'address'), (5, 'attributes'), (6, 'categories'), (7, 'city'), 
#(8, 'review_count'), (9, 'name'), (10, 'longitude'), (11, 'state'), 
#(12, 'stars'), (13, 'latitude'), (14, 'postal_code'), (15, 'type')]
    
if __name__ == "__main__":
    print("START")
    fname = "../dataset-examples-master/yelp_academic_dataset_business.csv"
    f = open(fname, 'r', encoding = 'utf8')
    
    # ofname = "filtered_small_business.csv"
    # of = open(ofname, 'w', newline = '')
    # writer = csv.writer(of)
    
    reader = csv.reader(f)

    x = 0
    d = dict()
    

    
    #get_attrib(reader, d, x)
    get_general(reader, d, x, 7)
    #get_state(reader, d, x)
    #eval_state(d)
    
    #     except:
    #         pass  
    d = sorted(d.items(),key = lambda x: (x[1], x[0]), reverse = True)
    for i in d[:10]:
        print(i)
    print()
    for i in d[-10:]:
        print(i)
    #for number of reviews the business has (30 to 50)
    # for k,v in d:
    #     if int(k) <= 50 and int(k) >= 30:
    #         print(k,v)
    
    
        
    # a = ['fame', 5, 'join us', [1,2,3]]
    # b = ['green\t f', 26, 'bring,', [6,2,6]]
    # writer.writerow(a)
    # writer.writerow(b)
    
    
    #reads and prints everything
    # for row in reader:
    #     print(row)   
    print("HERE")
    f.close()
    # of.close()
    print("END")
    
    f2 = "./dataset-examples-master/small_business.csv"
