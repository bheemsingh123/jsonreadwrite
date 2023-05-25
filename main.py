# https://docs.python.org/3/library/json.html?highlight=json%20encoder


# transfer and receive data between a web browser and a server in JSON format. The JSON is a simple text that is written in the javascript object notation mostly used as a syntax for storing and exchanging data.JSON package that can be used to work with JSON data,,,,,we can work with JSON objects including parsing, serializing, deserializing, 

# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)



# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

# json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)






# javascript object notation
#======================
import json




#=========================================
id = int(input("enter id :"))
FN = input("enter first name :")
LN = input("enter last name :")

user = {
    "id" : id,
    "FN" : FN,
    "LN" : LN
}

# data = json.dumps(user)  # serialize  the data
# file = open("a.json","a")
# file.write(data)
# file.close()
s=(":",",")
with open("a.json","a") as f:
    json.dump(user,f,indent=6,separator=s)
# =============================================================================

file = open("a.json","r")
x=file.read()  #in str format
print(x)
final_data = json.loads(x)# deserialize the data  #convert str to object so that we can access data by key
for x in final_data :
    print(x)
    print(x["id"])
    print(x["FN"])
    print(x["LN"])

print(final_data)
print(final_data[0])
print(final_data[1])
print(final_data[2])

print(final_data[0]["id"])
# print(final_data[1]["id"])
# print(final_data[2]["id"])

if final_data[0]["id"] == 2:
    print("true")
else:
    print("false")

