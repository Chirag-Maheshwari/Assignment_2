ans = [[0 for x in range(0,101)] for y in range(0,101)] 
width= int(input('Enter width: '))
height= int(input('Enter height: '))
m= int(input('Enter m: '))
for i in range(0,m):
    # a,b,c,d are points
    a= int(input('Enter a: '))
    b= int(input('Enter b: '))
    c= int(input('Enter c: '))
    d= int(input('Enter d: '))
    # -1 for down
    # -2 for left
    if (a==c):
        if (b>d):
            ans[a][b]=-1
        else:
            ans[c][d]=-1
    else:
        if (a>c):
            ans[a][b]=-2
        else:
            ans[c][d]=-2
for i in range(0,width+1):
    for j in range(0,height+1):
        if(i==0 and j==0):
            ans[i][j]=1
        else:
            if(ans[i][j]==0):
                if(j!=0):
                    ans[i][j]+=ans[i][j-1]
                if(i!=0):
                    ans[i][j]+=ans[i-1][j]
            elif(ans[i][j]==-1):
                if(i==0):
                    ans[i][j]=0
                else:
                    ans[i][j]=ans[i-1][j]
            
            elif(ans[i][j]==-2):
                if(j==0):
                    ans[i][j]=0
                else:
                    ans[i][j]=ans[i][j-1]

print ans[width][height]
