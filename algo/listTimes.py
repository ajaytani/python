import sys
#list of strings of military time
# 00:00 23:59
# h of 0 to 23
# m of 0 to 59
lst = ['00:23','01:30','01:59','22:34','21:59','00:40']
n = len(lst)
T = [[0 for i in range(60)] for i in range(24)]
Timelist = [0]*(1440)
for i in lst:
    h, m = [int(x) for x in i.split(':')]
    T[h][m] = 1
    Timelist[h*60+m] = 1

print(Timelist)

minCount = sys.maxsize
list = []
currpos=0
for i in range(1440):
    if Timelist[i] ==1:
        list.append(i)

currmin = sys.maxsize
for i in range(1,len(list)):
    if currmin > list[i] -list[i-1]:
        currmin = list[i] -list[i-1]
        currrightpos = list[i]
        currleftpos = list[i-1]

if currmin > list[0] + 1440 -list[-1]:
    currmin = list[0] + 1440 -list[-1]
    currleftpos = list[-1]
    currrightpos = list[0]

print(currmin)




