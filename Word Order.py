n=int(input())
words=[input() for i in range(n)]
occur={}
for word in words:
    occur[word]=0
for word in words:
    occur[word]+=1
print(len(occur))
occurences=occur.values()
for i in occurences:
    print(i,end=" ")