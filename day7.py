'''7일차 1번 문제: 문자 블록 합치기

🔹 문제 설명
문자열이 주어졌을 때, 연속된 동일한 문자의 블록을 찾고, 각 블록의 문자와 길이를 튜플 형태로 리스트로 반환하세요.
단, 결과는 블록이 등장한 순서대로 출력되어야 합니다.

🔹 입력 형식
	•	문자열 한 줄 (예: aaabbcdddeaa)

🔹 출력 형식
	•	다음 형식의 리스트 출력:
[('a', 3), ('b', 2), ('c', 1), ('d', 3), ('e', 1), ('a', 2)]'''

a=input().lower()
firs = a[0]
cnt = 1
li = []
for i in a[1:]:
    if i == firs:
        cnt+=1
    else:
        li.append([firs,cnt])
        firs = i
        cnt = 1
li.append([firs,cnt])
print(li)

from itertools import groupby
a = input().lower()
li = [(st, len(list(cnt))) for st,cnt in groupby(a)]
print(li)

'''7일차 2번 문제: 문자 압축 비율 분석기

🔹 문제 설명
문자열을 입력받아, 같은 문자가 연속될 경우 해당 문자의 개수를 붙여 압축한 문자열을 생성하세요.
그리고 원래 문자열 대비 압축된 문자열의 길이 비율을 출력하세요 (소수 둘째 자리까지).

⸻

🔹 입력 형식
	•	문자열 한 줄 (소문자 알파벳, 길이 1 이상)

🔹 출력 형식
	1.	압축된 문자열 출력
	2.	압축 비율 (압축 후 길이 / 원래 길이, 소수 둘째 자리까지)'''

from itertools import groupby
n = input()
nn = [(st,len(list(cn)))for st,cn in groupby(n)]
nnn = ''
for s in nn:
    if s[1] == 1:
        nnn += s[0]
    else:
        nnn += s[0] + str(s[1])
print(nnn)
print(f'{len(nnn)/len(n):.2f}')

'''7일차 3번 문제: 가장 긴 숫자 연속 구간 추출기

🔹 문제 설명
문자열을 입력받아, 그 안에 있는 연속된 숫자 구간들 중에서 가장 긴 것을 찾아 출력하세요.
동일한 길이의 숫자 구간이 여러 개면, 가장 먼저 등장한 구간을 출력합니다.

⸻

🔸 입력 형식
	•	문자열 한 줄 (예: a12bc345def67gh8901ij)

🔸 출력 형식
	•	가장 긴 숫자 구간을 그대로 출력 (예: 345)'''
n = input()
nums= ''
for i in n:
    if i.isalpha():
        nums+=' '
    elif i.isdigit():
        nums+=i
nums = nums.split(' ')
if nums:
    print(max(nums, key=len))
else:
    print('NONE')

nnnnn = re.findall(r'\d+',n)
print(max(nnnnn, key=len))

'''7일차 5번 문제: 가장 많이 등장한 숫자 그룹 찾기

🔹 문제 설명
문자열을 입력받고, 그 안에서 숫자가 연속해서 등장하는 모든 숫자 그룹을 추출하세요.
가장 자주 등장한 숫자 그룹(문자열 기준)을 찾아 출력하세요.
(여러 개면 사전순으로 가장 앞선 것을 출력)

⸻

🔹 입력 형식
	•	문자열 한 줄
예: "abc123def456ghi123jkl456123"

⸻

🔹 출력 형식
	•	가장 많이 등장한 숫자 그룹 출력 (예: 123)
	•	동일 빈도의 그룹이 여러 개면 사전순 출력'''
import re
from collections import Counter
n = input()
nn = re.findall(r'\d+',n)
nnn = Counter(nn)
s = sorted(nnn.items() ,key= lambda x: (-x[1],x[0]))
print(s[0][0])