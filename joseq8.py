# Q8.Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai 
# jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary 
# honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke
#  aapko ek json file create karni hai? Jaise ki niche diya hai.

import json
# list2=["komal","trainer","24","2400",] 
# list3=["anuradha","HR","25","40000"]
# list4=["Abhishek","manager","29","63000"]  
keys=["name","designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
e={}
list1=["neelam","programer","24","2400",]
for i in range(len(keys)):
    emp1[keys[i]]=list1[i]
e["emplyee1"]=emp1
list2=["komal","trainer","24","20000"]
for i in range(len(keys)):
    emp2[keys[i]]=list2[i]
e["emplyee2"]=emp2
list3=["anuradha","HR","25","40000"]
for i in range(len(keys)):
    emp3[keys[i]]=list3[i]
e["emplyee3"]=emp3
list4=["Abhishek","manager","29","63000"]
for i in range(len(keys)):
    emp4[keys[i]]=list4[i]
e["emplyee4"]=emp4
with open ("q8.json","w")as f:
    json.dump(e,f,indent=5)