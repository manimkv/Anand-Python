#json encoding

def json_encode(data):
   if isinstance(data, bool):
      if data:
         return "true"
      else:
         return "false"
   elif isinstance(data, (int, float)):
      return str(data)
   elif isinstance(data, str):
      return '"' + escape_string(data) + '"'
   elif isinstance(data, list):
      return "[" + ", ".join(json_encode(d) for d in data) + "]"
   elif isinstance(data,dict):
      return "{" + ", ".join(json_encode(k)+':'+json_encode(v) for k,v in data.items())+"}"
   else:
      raise TypeError("%s is not JSON serializable" % repr(data))
def escape_string(s):
	s = s.replace('"', '\\"')
	s = s.replace("\t", "\\t")
	s = s.replace("\n", "\\n")
	return s
print json_encode("[1,2.3,'list',['a','b','c'],{'dict':2,'x':'y'}]")
