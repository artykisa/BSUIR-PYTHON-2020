import random
import tempfile
def len_of_file(filename):
    i=0
    with open(filename) as f:
        for lines in f:
            i+=1
    return i
def getline(filename, num):
    file=open('filename','w')
    i=0
    for line in file:
        if i==num:
            return line
        i+=1
def changelineinfile(filename1,num,str1):
    i=0
    temp=tempfile.NamedTemporaryFile
    with open(filename1.name,'w+') as file1:
        with open(filename2.name,'w+') as file2:
          for lines in file1:
             if(i==num):
                file2.write(str1)
             else:
                file2.write(lines)                            
             i+=1
   #       filename1=temp
   # return filename1
def setvalue(filename1,filename2,num1,num2):
     i=j=0
     with open(filename1.name,'w+') as file1:
            for lines in file1:
                if(i==num1):
                    str1=lines
                i+=1
     with open(filename2.name,'w+') as file2:
          for lines in file1:
                if(j==num2):
                    str2=lines
                j+=1
     changelineinfile(filename1,num1,str1)
    # return filename1
def change(filename1,filename2,num1,num2):
    i=j=0
    with open(filename1.name,'w+') as file1:
            for lines in file1:
                if(i==num1):
                    str1=lines
                i+=1
    with open(filename2.name,'w+') as file2:
          for lines in file1:
                if(j==num2):
                    str2=lines
                j+=1
    changelineinfile(filename1,num1,str1)
    changelineinfile(filename2,num2,str2)
def mergesort(str):
    print("Merge Sort");
    mylist=[]
    str=str.split();
    for x in str:
        mylist.append(int(x));
    merge(mylist);
    print(mylist);
def merge(myfile):
     print("opa",myfile)
     leng=len_of_file(myfile)
     if leng >1: 
        mid = leng//2 #here
        L = tempfile.NamedTemporaryFile(delete=False)
        R = tempfile.NamedTemporaryFile(delete=False)
        i=0
        with open(myfile, 'r', encoding='utf-8') as g:
         with open(L.name, 'w+', encoding='utf-8') as L:
          with open(R.name, 'w+', encoding='utf-8') as R:
            for line in g:
                 if i<=leng:
                     L.write(line)
                 else:
                     R.write(line)
                 i+=1
        merge(L.name) 
        merge(R.name)  
        i = j = k = 0
        print("jopa")
        while i < len_of_file(L.name) and j < len_of_file(R.name): 
            if long(getline(L,i)) < long(getline(R,j)): 
                setvalue(myfile,L,k,j)
                #mylist[k] = L[i] 
                i+=1
            else: 
                setvalue(myfile,R,k,j)
                #mylist[k] = R[j] 
                j+=1
            k+=1
        print("jopa2")
        while i < len_of_file(L.name): 
            setvalue(myfile,L,k,j)
            #mylist[k] = L[i] 
            i+=1
            k+=1   
        print("jopa3")
        while j < len_of_file(R.name): 
            setvalue(myfile,R,k,j)
            #mylist[k] = R[j] 
            j+=1
            k+=1
merge("nums.txt")
#print(len_of_file("nums2.txt"))
#tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)¶
