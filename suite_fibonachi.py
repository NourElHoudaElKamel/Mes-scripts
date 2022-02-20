fibo =[0,1]
i=0
while len(fibo) < 20:
    fibo.append(fibo[i]+fibo[i+1])
    i = i + 1
    print(fibo)
print(len(fibo))