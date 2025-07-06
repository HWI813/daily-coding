'''6일차 1번 문제: 중복 제거 후 정렬된 숫자 집합

🔹 문제 설명
정수들이 섞인 문자열을 입력받아, 이 중 숫자만 추출한 후, 중복을 제거하고, 오름차순으로 정렬된 리스트를 출력하세요.

🔹 입력 형식
	•	문자열 한 줄 (예: ab12c3d2a1e4f1)

🔹 출력 형식
	•	숫자만 추출하여, 중복 없이 오름차순 정렬한 결과를 리스트 형태로 출력 (예: [1, 2, 3, 4])'''
n= input()
s = sorted(set([int(x) for x in n if x.isdigit()]))

s
''' 6일차 2번 문제: 숫자 빈도 세기

🔹 문제 설명
문자열을 입력받아, 문자열 안에 등장하는 숫자(0~9) 각각의 등장 횟수를 세어,
숫자 순서대로 숫자:횟수 형식으로 출력하세요.
단, 등장하지 않은 숫자는 출력하지 마세요.

⸻

🔸 입력 형식
	•	문자열 한 줄 (영문자와 숫자가 섞여 있음)

🔸 출력 형식
	•	숫자:횟수 형식으로 숫자 순서대로 출력 (줄마다 하나씩)'''
from collections import Counter
n = input()
n = ([int(x) for x in n if x.isdigit()])
nn = Counter(n)
wnn = sorted(nn.items(), key=lambda x: x[0])
for x,y in wnn:
    print(f'{x}:{y}') 

'''6일차 3번 문제: 가장 많이 등장한 숫자

🔹 문제 설명

문자열을 입력받고, 그 안에 포함된 숫자(0~9) 중 가장 많이 등장한 숫자를 출력하세요.
만약 등장 횟수가 같은 숫자가 여러 개라면, 숫자가 작은 것부터 출력하세요.

⸻

🔸 입력 형식
	•	문자열 한 줄 (예: a12b334cc99)

🔸 출력 형식
	•	가장 많이 등장한 숫자(들)를 한 줄에 하나씩 출력'''
n = input()
su = [int(x) for x in n if x.isdigit()] 
cnt = dict()
for ch in su:
    cnt[ch] = cnt.get(ch,0)+1
mos = max(cnt.values())
cnt = sorted(cnt.items())

for x in cnt:
    if x[1] == mos:
        print(x[0])

'''6일차 4번 문제: 문자-숫자 페어 추출기

🔹 문제 설명
문자열을 입력받아,
영문자와 숫자가 번갈아 등장하는 문자-숫자 쌍만 추출하여 출력하세요.

예를 들어, 입력이 a2b3x7q 라면 다음과 같이 추출됩니다:
	•	a2
	•	b3
	•	x7

숫자가 먼저 나오거나, 문자나 숫자가 혼자 있는 경우는 무시합니다.

⸻

🔹 입력 형식
	•	문자열 한 줄 (예: a2b3x7q9z)

🔹 출력 형식
	•	조건에 맞는 문자-숫자 쌍을 한 줄에 하나씩 출력

⸻
'''
n = input()
for i in range(len(n)-1):
    if n[i].isalpha():
        if n[i+1].isdigit():
            print(n[i]+n[i+1])

'''6일차 5번 문제: 알파벳-숫자 페어 합산기

🔹 문제 설명
문자열을 입력받아 알파벳과 숫자가 번갈아 등장하는 쌍을 찾아,
모든 숫자의 합을 계산하세요.

알파벳 뒤에 오는 숫자만 유효합니다. 숫자가 여러 자리일 경우도 고려하세요.

⸻

🔸 입력 형식
	•	문자열 한 줄 (예: a12b3c45d)

🔸 출력 형식
	•	숫자들의 합을 출력 (예: 12 + 3 + 45 = 60 → 출력은 60)'''

n = input()
num = ''
for ch in n:
    if ch.isdigit():
        num = num + ch
    else:
        num += ' '
num = (num).strip().split(' ')
nn = 0
for i in num:
    nn+= int(i)

nn