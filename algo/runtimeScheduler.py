steps = [1,2,3]
n = 7
T = [[0 for i in range(n+1)] for j in range(3)]
for i in range(3):
    T[i][0] = 1
i = j = 0
print(T)
while i < 3:
    for j in range(1,n+1):
        if j >=steps[i]:
            T[i][j] = T[i-1][j] + T[i][j-steps[i]] 
        else:
            T[i][j] = T[i-1][j]
    i+=1
print(T)
print (T[2][n])