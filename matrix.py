# -*- coding: utf


x = [[1,2,3],[5,7,3],[5,7,3]]
y = [[5,7,1],[3,4,9],[1,5,7]]
 
sonuç = [[0,0,0] , [0,0,0] , [0,0,0]]
 
for i in range(len(x)):
    for j in range(len(y)):
        sonuç[i][j] = x[i][j]+y[i][j]
         
print(sonuç)         