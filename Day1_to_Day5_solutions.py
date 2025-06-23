# 1번
def solution(numbers):
    answer = 0
    n = len(numbers) // 2
    if len(numbers) % 2 != 1:
        answer = (numbers[0] + numbers[-1]) * n / 2
    else:
        answer = ((numbers[0] + numbers[-1]) * n) + numbers[n] / 2
    return answer

# 2번
N = int(input())
num = list(map(int, input().split(' ')))
print(min(num), max(num))

# 2번 확장 (min/max 직접 구현)
max_val, min_val = num[0], num[0]
for i in num:
    if i >= max_val:
        max_val = i
    if i <= min_val:
        min_val = i 
print(min_val, max_val)

# 3번
numb = []
for _ in range(9):
    n = int(input())
    numb.append(n)
print(max(numb))    
print(numb.index(max(numb)) + 1)

# 4번
A = int(input())
B = int(input())
C = int(input())
su = str(A * B * C)
kkk = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in su:
    if i in kkk:
        kkk[i] += 1
for j in kkk.values():
    print(j)

# 5번
bin = set()
for _ in range(10):
    s = int(input())
    bin.add(s % 42)
print(len(bin))

