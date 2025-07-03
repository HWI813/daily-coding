n = list(input())
i = [n[-x] for x in range(1,len(n)+1)]
print(''.join(i))
n = input().replace(' ','')
print(n[::-1])

#2번
n = input().split(' ')
n.sort(key=lambda x: (len(x),x))
print(n[-1])

#3번
n = int(input())
word = {input() for _ in range(n)}
n_word=sorted(word, key=lambda x: (len(x),x))
for i in n_word:
    print(i)

#4번
a = int(input())
word = {input() for _ in range(a)}
n_word = sorted(word, key=lambda x: (-len(x), sum(1 for ch in x if ch in 'aeiou'), x))

for i in n_word:
    print(i)
#5번
from collections import Counter
a = int(input())
word = {input() for _ in range(a)}
w = Counter(len(x) for x in word)
long = max(w, key=w.get)
n_word = sorted([x for x in word if len(x)==long])
for i in n_word:
    print(i)


#6번
n_w =[]
for x in word:
    leng = len(x) //2 
    if len(x) %2 != 0:
        if x[:leng]== x[-1:leng:-1]:
            n_w.append(x)
    else:
        if x[:leng]== x[-1:leng-1:-1]:
            n_w.append(x)
n_w = sorted(n_w)
for t in n_w:
    print(t)