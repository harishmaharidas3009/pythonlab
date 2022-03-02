str=input("Enter a string:")
def adding(str):
    lenght=len(str)
    if str[-3:]=='ing':
        str+='ly'
        return str
    else:
        str+='ing'
        return str
print(adding(str))
