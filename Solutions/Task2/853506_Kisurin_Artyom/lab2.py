import tempfile

def len_of_file(filename):
    i=0
    with open(filename) as f:
        for lines in f:
            i+=1
    return i


def getline(filename, num):
    i=0
    with open(filename,'r', encoding='utf-8') as file1: 
        for line in file1:
            if i==int(num):
              return line
            i+=1


def changelineinfile(filename1,num,str1):
    i=0
    temp=tempfile.NamedTemporaryFile
    with open(filename1,'r') as file1:
        with open(temp.__name__,'w') as file2:
          for lines in file1:
             if(i==num):
                file2.write(str1)
             else:
                file2.write(lines)                            
             i+=1
    with open(filename1,'w') as file1:
        with open(temp.__name__,'r') as file2:
          for lines in file2:       
                file1.write(lines)                            


def setvalue(filename1,filename2,num1,num2):
     i=j=0
     str2=""
     with open(filename2,'r') as file2:
          for lines in file2:
                if(j==num2):
                    str2=lines
                j+=1
     changelineinfile(filename1,num1,str2)

def merge(myfile):
     leng=len_of_file(myfile)
     if leng >1: 
        mid = leng//2 #here
        L = tempfile.NamedTemporaryFile(delete=False)
        R = tempfile.NamedTemporaryFile(delete=False)
        i=1
        with open(myfile, 'r', encoding='utf-8') as g:
         with open(L.name, 'w', encoding='utf-8') as L:
          with open(R.name, 'w', encoding='utf-8') as R:
            for line in g:
                 if i<=mid:
                     L.write(line)
                 else:
                     R.write(line)
                 i+=1
        merge(L.name) 
        merge(R.name)  
        i = j = k = 0
        while i < len_of_file(L.name) and j < len_of_file(R.name): 
            if float(getline(L.name,i)) < float(getline(R.name,j)):
                setvalue(myfile,L.name,k,i)
                i+=1
            else:
                setvalue(myfile,R.name,k,j)
                j+=1
            k+=1
        while i < len_of_file(L.name):
            setvalue(myfile,L.name,k,i)
            i+=1
            k+=1
        while j < len_of_file(R.name):
            setvalue(myfile,R.name,k,j)
            j+=1
            k+=1
if __name__ == "__main__":
    print("Start sort...")
    merge("nums.txt")
    print("Sort completed")
