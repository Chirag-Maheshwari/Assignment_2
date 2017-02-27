def max(a,b):
    return a if a>b else b

n= int(input('Enter n: '))
arr=[0]*n;
res_pos=[0]*n;
res_neg=[0]*n;
for i in range(0,n):
    arr[i]= int(input('Enter array element: '))
for i in range(0,n):
    res_neg[i]=0
    res_pos[i]=0
    for j in range(i-1,-1,-1):
        diff=arr[i]-arr[j]
        if(diff>0):
            res_pos[i]=max(1+res_neg[j],res_pos[i])
        elif(diff<0):
            res_neg[i]=max(1+res_pos[j],res_neg[i]) 
print max(res_neg[n-1],res_pos[n-1])+1

