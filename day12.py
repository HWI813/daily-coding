'''12일차 1번 문제: 최소 제거 문자 수

🔹 문제 설명

문자열이 주어졌을 때, 가장 자주 등장한 문자 2개를 제외한 나머지 문자의 등장 횟수의 합을 구하세요.

🔸 입력 형식
	•	문자열 S (영문 소문자, 길이 1 이상 1000 이하)

🔸 출력 형식
	•	가장 많이 나온 문자 2개를 제외한 삭제된 문자 수 (정수 하나)

⸻
'''
from collections import Counter
s = Counter(input())
sss = sorted(s.items(), key=lambda x: x[1], reverse=True)
num=0
if sss:
    for x,y in sss[2:]:
        num+=y
else:
    print('NONE')
print(num)

'''12일차 2번 문제: K-길이 구간 내 다양한 문자 수

🔹 문제 설명
	•	문자열 S가 주어졌을 때, 길이가 K인 모든 연속 부분 문자열에 포함된 서로 다른 문자 수를 센다.
	•	이 중 가장 다양한 문자 수를 가진 구간의 문자 수를 출력하시오.

🔸 입력
	•	문자열 S
	•	정수 K

🔸 출력
	•	길이 K 구간 중 가장 다양한 문자 수 (서로 다른 문자 수)'''

s = input()
k = int(input())
ma = 0
for i in range(len(s)-k+1):
    st = s[i:i+k]
    if (len(set(st))) >= ma:
        ma = len(set(st))
print(ma)

'''12일차 3번 문제: 특정 문자 제거 후 압축 길이

🔹 문제 설명
문자열 s가 주어집니다. 이 문자열에서 한 문자를 선택해 전부 제거한 후, 남은 문자열을 연속된 문자 압축합니다.
이때 압축한 문자열의 길이를 출력하세요.
가장 짧은 압축 길이를 출력하시오.

🔹 입력 형식
	•	첫 줄: 문자열 s (1 ≤ len(s) ≤ 1000)

🔹 출력 형식
	•	특정 문자를 하나 제거했을 때 얻을 수 있는 최소 압축 길이 (정수 하나)'''
from itertools import groupby
from collections import Counter
s = input()
sss = []
ssss =[(st,len(list(l))) for st,l in groupby(s)]
ss = ''
for i,le in ssss:
    ss +=i+(str(le))
    sss.append(i)
xxx = max(Counter(sss).items(), key=lambda x: x[1])
d = xxx[1]
print(int(len(ss)/2 - d))

''' 12일차 4번 문제

문자열을 입력받아, 연속으로 3번 이상 등장한 문자 블록의 수를 출력하세요.

예를 들어, 입력이 aaabbbccaaaadd라면 aaa, bbb, aaaa → 총 3개 블록입니다.

단, 한 문자에 대해 여러 블록이 존재해도 각각 카운트합니다.'''
s = input()
ssss =[(st,len(list(group))) for st,group in groupby(s) if (l :=len(list(group))>=3)]
print(len(ssss))

'''12일차 5번 문제

🔸 문제:

어떤 문자열 s가 주어집니다. 이 문자열에서 서로 다른 문자가 정확히 k개 포함된 가장 긴 부분 문자열의 길이를 구하세요.

단, 영어 소문자(a~z)만 포함됩니다.

⸻

🔹 입력:
	•	문자열 s (1 ≤ len(s) ≤ 100,000)
	•	정수 k (1 ≤ k ≤ 26)

⸻

🔹 출력:
	•	조건을 만족하는 가장 긴 부분 문자열의 길이'''
from collections import defaultdict
s = input()
k = int(input())
d = defaultdict(int)
left = 0
max_len = 0
for right in range(len(s)):
    d[s[right]] += 1
    while len(d) > k:
        d[s[left]] -= 1
        if d[s[left]] == 0:
            del d[s[left]]
        left += 1
    max_len = max(max_len, right -left + 1)
print(max_len)
        
