data = input()

def count(data):
    num=0
    for i in range(len(data)):
        if int(data[i])%2==1:
            num+=1
    return num
minV = 1e9
maxV = 0
def f(data,odd_n):
    global minV,maxV
    if len(data) == 1:
        minV = min(minV,odd_n)
        maxV = max(maxV,odd_n)
        return data[0]
    elif len(data) == 2:
        new = int(data[0])+int(data[1])
        new = str(new)
        f(new,odd_n+count(new))
    else:
        n = len(data)
        for i in range(1,n-1):
            for j in range(i+1,n):
                new = int(data[:i])+int(data[i:j])+int(data[j:])
                new = str(new)
                f(new,odd_n+count(new))
f(data,count(data))               
print(minV,maxV)