# Q.2 Python object ko json data main convert karne ka program likho? 

import json
dict1={
    "name": "David",
    "class":"I",
    "age": 6  
 }

with open ("q2.json","w")as f:
    json.dump(dict1,f,indent=5)