# Q.1 Json data ko python object main convert karne ka program likho?. Example: 

import json
dict1={
    "Name":"Ram", 
    "Class":"IV", 
    "Age":9 
}
file= open ("q1.json","r+")
a=json.load(file)
print(a)
file.close()
