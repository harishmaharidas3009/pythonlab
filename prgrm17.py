dict1={"a":200,"b":500,"c":100}
dict2={"x":50,"y":30,"z":200}
print("dictionary1=",dict1)
print("dictionary2=",dict2)
dict=dict1.copy()
dict.update(dict2)
print("merged dictionary is:",dict)
