import math
class MyError(Exception):
    def __init__(self, text):
        self.txt = text
 
class vector:
    vec=[]
    def __init__(self,n):
        self.vec=n
        self.num=len(self.vec)
    @staticmethod
    def add(vector1,vector2):
        print("add")
        try:
            if len(vector1.vec)!=len(vector2.vec):
                 raise MyError("Wrong vectors in add!")
            ret=[]
            j=0
            for i in vector1.vec:
                   ret.append(vector1.vec[j]+vector2.vec[j])
                   j+=1
            return ret
        except MyError as mr:
                 print(mr)
        

    @staticmethod
    def sub(vector1,vector2):
        print("sub")
        try:
            if len(vector1.vec)!=len(vector2.vec):
                 raise MyError("Wrong vectors in sub!")
            ret=[]
            j=0
            for i in vector1.vec:
                   ret.append(vector1.vec[j]-vector2.vec[j])
                   j+=1
            return ret
        except MyError as mr:
                 print(mr)
        
  
    def multconst(self,cons):
        print("multconst")
        j=0
        for i in self.vec:
           self.vec[j]*=cons
           j+=1
   
    @staticmethod
    def scalar(vector1,vector2):
        try:
            if len(vector1.vec)!=len(vector2.vec):
                 raise MyError("Wrong vectors in scalar!")
            print("scalar")
            ret=0
            j=0
            for i in vector1.vec:
                    ret+=vector1.vec[j]*vector2.vec[j]
                    j+=1
            return ret
        except MyError as mr:
                 print(mr)
       

    def Equal(self,vector2):
        print("Euqal")
        if len(self.vec)!=len(vector2.vec):
            return False
        j=0
        for i in self.vec:
           if i!=vector2.vec[j]:
               return False
           j+=1
        return True

    def getbyindex(self,index):
        print("getbyindex")
        try:
            if len(self.vec)<=index:
                 raise MyError("Wrong index!")
            j=0
            for i in self.vec:
                 if j==index:
                     return i
                 j+=1
        except MyError as mr:
                 print(mr)

        
   
    def tostring(self):
        print("tostring")
        s=""
        for i in self.vec:
            s+=str(i)+','
        s=s[:len(s)-1]
        return s
    
    def lengh(self):
        print("length")
        ret=0
        temp=0
        j=0
        for i in self.vec:
           temp+=self.vec[j]**2
           j+=1
        ret=math.sqrt(temp)
        return ret

if __name__ == "__main__":
    vec=vector([1,2,3])
    vec2=vector([5,4,6,7])
    vec3=vector([1,2,3])
    print(vector.scalar(vec,vec3))
    print(vector.scalar(vec,vec2))
    print(vec.Equal(vec3))
    print(vec.Equal(vec2))
    print(vec.tostring())
    print(vec.getbyindex(2))
    print(vec.getbyindex(10))
    vec.multconst(2)
    print(vec.vec)
    print(vector.add(vec,vec2))
    print(vector.sub(vec,vec2))
    print(vec3.lengh())
    try:
        a=0
        if a==0:
            raise MyError("You give negative!")
        print("dfdf")
    except MyError as mr:
        print(mr)