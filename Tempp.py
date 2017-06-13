def replicate(times, data):
  value = []
  if type(times) is str or data is " ":
    raise ValueError ("Invalid Input")
  elif times > 0 and data is not " ":
   for x in range(times):
     value.append(data)
     return value
  elif times <= 0:
    return value
H = replicate(5,"x")
print(str(H))
