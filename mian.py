from daydata import daydata
from cacl import cacl
from position import position
print("开始运行")
f = open("JL9(1).txt")

position = position()

cacl = cacl(position)
#每一行都是一个结构体 时间，收盘价格 m20价格
line = f.readline()
i = 0

while line:  
    lineArr = line.split("\t")
    #print(lineArr)

    line = f.readline()

    i +=1
    if i<24:
        continue

    data = daydata(lineArr)
    cacl.work(data)
    
    print(data)
    
f.close()

#print(cacl.recordList)

backNum = 0.0
preRecord = 0.0
maxPassNum = 0.0
maxDepth = 0.0
earnList = []

print(cacl.recordList)

for record in cacl.recordList:
    if not preRecord:
        preRecord = record
        maxPassNum = record
        continue

    if maxPassNum < record:
        maxPassNum = record
    else:
        print(str(record))
        print(str(maxPassNum))
        nowDepth = (record/maxPassNum-1)*100.0
        if nowDepth < maxDepth:
            maxDepth = nowDepth
        print('当前回退了多少:'+str((record/maxPassNum-1)*100.0))

    earn = (record-preRecord)/preRecord
    preRecord = record
    earnList.append(earn)

print(earnList)
print(len(cacl.recordList))
print(len(earnList))
print('最大回撤:'+str(maxDepth))
print('净值:'+str(cacl.recordList[-1]))







