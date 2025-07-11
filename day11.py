'''11일차 1번 문제: 최대 알파벳 연속구간 길이 찾기

🔸 문제 설명
소문자로 이루어진 문자열이 주어졌을 때, 연속으로 나열된 같은 알파벳 구간 중에서 가장 긴 구간의 길이를 구하세요.

예를 들어, "aaabbccaaaaaadd" 가 주어지면:
	•	‘a’ → 3,
	•	‘b’ → 2,
	•	‘c’ → 2,
	•	‘a’ → 6,
	•	‘d’ → 2

따라서 정답은 6.

⸻

🔸 입력 형식
	•	소문자 문자열 (1 ≤ 길이 ≤ 1000)

🔸 출력 형식
	•	가장 긴 알파벳 연속 구간의 길이 (정수)
'''
from itertools import groupby
n =input()
nn = [(st, len(list(l))) for st,l in groupby(n)]
nn = sorted(nn, key= lambda x: -(x[1]))
if nn:
	print(nn[0][1])
else:
	print('NONE')
'''11일차 2번 문제: 최장 짝수 반복 문자 그룹

🔹 문제 설명

문자열이 주어졌을 때,
연속된 같은 문자들 중 반복 횟수가 짝수인 것 중 가장 긴 길이를 출력하세요.

조건:
	•	만약 짝수 길이의 그룹이 없다면 "NONE"을 출력하세요.

⸻

🔸 입력 형식
	•	영문 소문자 문자열 (길이 1 이상 1000 이하)

🔸 출력 형식
	•	가장 긴 짝수 반복 길이 (정수 하나) 또는 "NONE"

⸻
'''
from itertools import groupby
n =input()
nn = []
for st,l in groupby(n):
    g = list(l)
    if len(g) %2 == 0:
        nn.append([st,len(g)])
nn = sorted(nn, key = lambda x:-(x[1]))
if nn:
    print(nn[0][1])
else:
    print('NONE')

''' 11일차 3번 문제: 최장 서로 다른 문자 간격

🔹 문제 설명
문자열이 주어졌을 때,
같은 문자가 두 번 등장하는 모든 쌍 중, 그 사이에 끼어 있는 문자들의 수가 가장 많은 쌍을 찾고,
그 최대 간격을 출력하세요.

단, 같은 문자가 단 한 번만 등장하거나 쌍이 없으면 "NONE"을 출력하세요.

⸻

🔸 입력 형식
	•	영문 소문자 문자열 (1 ≤ 길이 ≤ 1000)

🔸 출력 형식
	•	최대 간격 (정수 하나) 또는 "NONE"'''
n = input()


di = dict()
for i in range(len(n)):
    if n[i] not in di:
        di[n[i]] = 1
    else:
        ll = n.index(n[i])
        di[n[i]] = i-1 - ll-1
print(max(di.values()) if max(di.values()) > 1 else 'NONE')

'''11일차 4번 문제: 연속된 동일 그룹의 총 길이 합

🔹 문제 설명

문자열이 주어졌을 때,
연속된 같은 문자들의 길이 합을 구하세요.
단, 한 번이라도 등장한 문자는 한 그룹만 인정합니다.

⸻

🔸 조건
	•	연속된 같은 문자 그룹만 계산
	•	같은 문자가 중간에 끊겼다가 다시 나오면 하나의 그룹만 포함
	•	예: "aaabbbaa" → 'a'는 두 번 나오지만 한 그룹만 인정 → 앞의 'aaa'만 포함

⸻

🔹 입력 형식

영문 소문자로 구성된 문자열 (길이 1 이상 1000 이하)

🔹 출력 형식

조건에 맞는 그룹들의 길이의 총합 (정수)
'''
n = input()
nn = [(st, len(list(l))) for st, l in groupby(n)]
ss = dict()
for x,y in nn:
    if y>=2:
        if x not in ss:
            ss[x] = y
        else:
            if ss[x] < y:
                ss[x] = y
            else:
                pass
print(sum(ss.values()))

'''11일차 5번 문제: 문자 교환 최소 횟수

⸻

🧩 문제 설명

주어진 문자열에서 서로 다른 두 문자만 남기고, 나머지 문자를 모두 제거하고자 한다.
이때, 제거할 문자들의 최소 삭제 횟수를 출력하는 프로그램을 작성하세요.

⸻

📌 조건
	•	남길 두 문자는 스스로 선택 가능함 (가장 유리한 두 문자 선택 가능)
	•	삭제해야 할 문자의 총 개수를 출력
	•	대소문자 구분 없음 (소문자만 주어짐)'''
from collections import Counter

n = input()
nn = Counter((n))
nnn = sorted(nn.items(),key= lambda x:(x[1]))

if len(nnn) >= 3:
    sum = 0
    for x,y in nnn[2:]:
        sum+=y
    print(sum)
else:
    print(0)
