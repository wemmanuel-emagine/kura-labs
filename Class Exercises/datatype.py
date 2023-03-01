# working with data types
import json

var1 = '{"name":"Peter Parker","age":21,"borough":"Queens"}'
print(type(var1))

var2 = json.loads(var1)
print(var2)

data = """
{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "uHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}

"""

# make a json parser class
# above example is the input for when the object is created
# make function that will output the number of healthy and unhealthy
# make a function that will create and output the list of unhealthy and healthy check names


class Json_Parser:
    def __init__(self,jsonfile):
        self.jsonfile = jsonfile
        self.diction = json.loads(self.jsonfile)
        print(self.diction)
    
    
    def healthy(self):
       for line in self.diction["Checks"]:
            print(line)


object1 = Json_Parser(data)  

# print(object1)
object1.healthy()