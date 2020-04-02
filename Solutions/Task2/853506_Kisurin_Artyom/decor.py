mydict={};
def toup(name):
        return name.upper()
def cached(func):
        def infunc(*args):           
           value=mydict.get(args,"no value")
           if value=="no value":
               value=func(*args)
               mydict.update({args:value});
           return value
        return infunc 
decorator = cached(toup)
if __name__ == "__main__":
   print(decorator("Artyom"))
   print(decorator("Artyom"))
   print(decorator("Artyom"))

