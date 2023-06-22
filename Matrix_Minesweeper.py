l=[[0,1,0,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
r=len(l)
c=len(l[0])


li=[]
for i in range(r):
    l2=[]
    for j in range(c):
        l2.append(j)
    li.append(l2)





m=0
for i in l:
    n=0
    for j in i:
        if (j==0)  and (l[m][n] ==0):
                count=0
                for a in range(m-1,m+2):
                    for b in range(n-1,n+2):
                        try:
                            if (l[a][b]!=0):
                                count=count+1
                                
                        except IndexError as ex:
                            continue
                li[m][n]=count
                
                
        else:
            li[m][n]="X"
        n=n+1 
    m=m+1
  
print(li)