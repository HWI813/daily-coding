'''5일차 1번 문제: 가장 많이 등장한 알파벳

🔹 문제 설명
문자열을 입력받아, 가장 많이 등장한 알파벳을 모두 출력하시오.
대소문자를 구분하지 않으며, 동률이 있을 경우 알파벳 순으로 출력합니다.

🔹 입력 형식
	•	문자열 한 줄 (공백 포함 가능, 알파벳과 공백만 있음)

🔹 출력 형식
	•	가장 많이 등장한 알파벳(소문자 기준)을 한 줄에 하나씩 출력'''
word = input().lower().replace(' ','')
cnt = Counter(word)
mos = sorted(cnt.items(), key=lambda x:(-x[1],x[0]) )
for i,_ in mos:
    print(i)


'''5일차 2번 문제: 등장 횟수 기준 필터링

🔹 문제 설명

문자열을 입력받고, 각 문자의 등장 횟수를 세어 딕셔너리로 저장하세요.
그 후 2번 이상 등장하는 문자만 사전 순으로 출력하세요.

🔹 입력 형식
	•	문자열 한 줄 (예: programmingisgreat)

🔹 출력 형식
	•	2번 이상 등장한 문자를 한 줄에 하나씩 사전 순으로 출력
	•	없다면 "None" 출력
'''
from collections import Counter
n = ''.join([ch for ch in input() if ch.isalpha()])
word = Counter(n)
wo = sorted([x[0] for x in word.items() if x[1] >= 2])
if wo:
    for x in wo:
        print(x)
else:
    print('None')

'''5일차 3번 문제: 공통 문자 추출기

🔹 문제 설명

두 개의 문자열을 입력받고, 두 문자열에 모두 존재하는 문자들만 추출하여 사전 순으로 한 줄에 하나씩 출력하세요.
단, 중복은 제거하며, 입력은 모두 소문자 알파벳으로만 구성됩니다.
'''
a = set(input())
b = set(input())
c = sorted([x for x in a if x in b])
if c:
    for i in c:
        print(i)
else:
    print('None')


'''5일차 4번 문제: 문자 그룹 압축기

🔹 문제 설명

문자열을 입력받고, 연속해서 등장하는 동일한 문자 그룹을 하나의 문자와 개수로 압축하여 출력하세요.
단, 개수가 1이면 생략합니다.

🔹 입력 형식
	•	문자열 한 줄 (예: aaabbccccd)

🔹 출력 형식
	•	압축된 문자열을 한 줄로 출력
(예: a3b2c4d)
'''
ip = input()
cnt = 1
fir = ip[0]
answer = ''
for i in ip[1:]:
    if i == fir:
        cnt +=1
    else:
        answer = answer + fir + (str(cnt) if cnt > 1 else '')
        fir = i
        cnt = 1
answer = answer + fir + (str(cnt) if cnt > 1 else '')
print(answer)

'''5일차 5번 문제: 가장 긴 동일 문자 그룹 찾기

🔹 문제 설명

문자열을 입력받고, 동일한 문자가 연속해서 등장하는 가장 긴 구간의 문자와 길이를 출력하세요.
만약 동일한 최대 길이의 구간이 여러 개면, 먼저 등장한 것을 출력하세요.

⸻

🔹 입력 형식
	•	문자열 한 줄 (예: aabbcccddddeeaa)

🔹 출력 형식
	•	문자:길이 형식으로 출력 (예: c:3)'''

ip = input()
cnt = 1
fir = ip[0]
segments = []

for i in ip[1:]:
    if i == fir:
        cnt += 1
    else:
        segments.append((fir, cnt))
        fir = i
        cnt = 1
segments.append((fir, cnt))
longest = max(segments, key=lambda x: x[1])
print(f'{longest[0]}:{longest[1]}')
