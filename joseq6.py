# Q6.Python object key unique key value ko access karne ka program likho?


import json
p={"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}
print("original python object:")
print(p)
json_obj=json.dumps(p)
print("\nunique key in a json object")
print(json_obj)