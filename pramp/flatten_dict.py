
def flatten_dictionary(dictionary):
  
  output = {}
  
  def dfs(dict1, keystring = ""):
    for key in dict1:
      value = dict1[key]
      if keystring:
          key = keystring+"."+key
      if isinstance(value, int) or isinstance(value, str):
        output[key] = value
      elif isinstance(value, dict):
        dfs(value, key)

      
  dfs(dictionary)
  return output


a = flatten_dictionary({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}})
print(a)

def flatten_dictionary(dictionary):
    items = []
    def flatten_dict(d, separator):
        for key, value in d.items():
            if isinstance(value,dict):
                items.extend(flatten_dict(value, separator=separator).items())
            else:
                items.append((key,value))
            return dict(items)
    return flatten_dict(dictionary, separator='.')