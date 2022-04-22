a=[[2,3,5],[4,5,6],[7,8,9]]
b=[[3,4,5],[7,8,9],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
     for j in range(len(a[0])):
          result[i][j]=a[i][j]+b[i][j]
for r in result:
     print(r)
