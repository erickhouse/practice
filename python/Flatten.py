#  {
#  a: 1,
#  b: 2,
#  c: {
#       d: 4,
#       e: {
#         g: 10,
#         h: 12
#       }
#  }

# }

# 
# {
#   a: 1,
#   b: 2,
#   c.d: 4,
#   c.e.g: 10,
#   c.e.h: 12
# }


nested =  { 'a': 1,'b': 2,'c': {'d': 4,'e': {'g': 10,'h': 12} } }

def flatten(nested):
    result = {}

    while(nested):
      for key,val in nested.items():
          if(type(val) is int):
            nested.pop(key)
            result[key] = val
          else:
            for child_key, child_val in val.items():             
              nested[key + '.' + child_key] = child_val
            nested.pop(key)

    return result


print(flatten(nested))

def test(cool):
    for c in cool:
        if c:
            print(c)
