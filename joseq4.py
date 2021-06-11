# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho? Example: Input 
# :- Output:- JSON data:

import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
   } 

a=json.dumps(a,indent=5,sort_keys=True)
print(a)
with open("q4.json","w")as f:
    f.write(a)