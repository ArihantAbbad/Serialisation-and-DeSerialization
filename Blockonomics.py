# Serialisation and DeSerialization of Flattend dictionary

def check(x):
    try:
        y = int(x)
        return y
    except:
        pass
    try:
        y = float(x)
    except:
        y  = x[1:-1] if x[0]==x[-1] and len(x)>1 else None
    return y
def DeSerialization(d):
    
    lst = list(d[1:-1].split(","))
    dic={}
    for i in lst:
        x = i.split(":")
        a = check(x[0])
        b = check(x[1])
        if a==None or b==None:
            return "Given input is not a valid dictionary"
        dic[a] = b
    else:
        return dic
def readFile(filename):
    file = open(filename,"r")
    string = file.read()
    return str(string)



def Serialization(filename,data):
    file = open(filename,"w+")
    file.write(str(data))
    file.close()
    print("Data saved successfully in",filename)
    
filename = "sample.txt"
data ='''{"a":1,"b":2,"c":3,4.1:"q",3:"f"}'''
print("Serialisation and DeSerialization of Flattend dictionary")

#serialization

Serialization(filename,data)

#deserialization

string = readFile(filename)
print(DeSerialization(string))






# Serialisation and DeSerialization of Nested dictionary 

def DeSerialization(filename):
    f = open(filename,"r")
    dic = f.read()
    try:
        dictionary = eval(dic)
    except:
        dictionary = "Given input is not a valid dictionary"
    return dictionary
        

def Serialization(filename,data):
    file = open(filename,"w+")
    file.write(str(data))
    file.close()
    print("Data saved successfully in",filename)

filename = "sample.txt"
data ='''{"a":1,"b":2,"c":3,4.1:"q",3:{"abc":"def",18:"v"}}'''
print("Serialisation and DeSerialization of Nested dictionary")

#serialization

Serialization(filename,data)

#deserialization

print(DeSerialization(filename))