
def ceil_index(arr,a,b,value):
    while((b-a)>1):
        m=a+(b-a)/2
        if(arr[m]>=value):
            b=m
        else:
            a=m
    return b;

 
def LISlength(arr,size):
    len=0
    LIS=[0]*size
    LIS[0]=arr[0]
    len=1
    for i in range(0,size):
        if(arr[i]>LIS[len-1]):
            LIS[len]=arr[i]
            len+= 1
        
        elif(arr[i]<LIS[0]):
            LIS[0]=arr[i];
        
        else:
            LIS[ceil_index(LIS,-1,len-1,arr[i])]=arr[i]
    return len;

 

t= int(input('Enter t: '))
while(t>0):
    maxi=0
    ans= 0
    n= int(input('Enter n'))
    arr=[0]*(2*n)
    for i in range(0,n):
        arr[i]= int(input('Enter arr element'))
        arr[i+n]=arr[i]
    
    for i in range(0,n):
        ans=LISlength(arr[i:i+n],n);
        if(ans>maxi):
            maxi=ans

    print maxi
    t-= 1