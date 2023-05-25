import json
from urllib.request import urlopen
with urlopen("https://jsonplaceholder.typicode.com/todos/1") as response:
    source = response.read()
# print(source)
a = json.loads(source)
print(json.dumps(a , indent = 4))