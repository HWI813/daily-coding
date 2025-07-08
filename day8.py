''' 8일차 1번 문제: 숫자 조합의 최대 합 구하기 (난이도: 골드5)

문제 설명
한 줄의 문자열이 주어집니다. 이 문자열에는 숫자(09)와 문자(az, A~Z)가 섞여 있습니다.
이 중 숫자만 추출하여 만들 수 있는 모든 두 숫자 조합의 합 중 가장 큰 값을 구하세요.
	•	단, 숫자는 중복 없이 한 번씩만 사용 가능
	•	숫자는 두 자리 수를 만들어야 하며, 첫 자리 숫자가 0이 되는 조합은 제외
	•	예: a9b8c7d → 숫자: [9,8,7] → 조합: 98, 97, 89, 87, 79, 78 → 합: 98+97=195, …, 최대 합은?

입력 형식
문자열 한 줄 (예: ab1c9x2y)

출력 형식
가장 큰 두 수 조합의 합 (예: 110)
'''
n = sorted(([int(x) for x in input() if x.isdigit()]),reverse=True)
print(int(str(n[0])+str(n[1]) )+int(str(n[1])+str(n[0])))

''' 8일차 2번 문제: 문자 그룹 반전 압축 (난이도: 골드 4)

🔹 문제 설명

주어진 문자열에서 연속된 동일한 문자 그룹을 찾아,
이를 반대로 뒤집은 후,
각 그룹의 문자와 등장 횟수로 압축한 문자열을 출력하세요.
(단, 등장 횟수가 1이면 생략)

🔸 입력 형식
	•	문자열 한 줄 (예: aaabbcccdeeaa)

🔸 출력 형식
	•	압축된 문자열을 한 줄로 출력
	•	예시 출력: 'a3b2c3e2d'
(→ 그룹은 aaabbccc → 뒤집으면 cccbb aaa → 각각 c3, b2, a3 순서로 압축
→ 이어서 처리된 e2, d1 → d는 1회이므로 그냥 d)'''
n = input()
nn = [(ch, len(list(l))) for ch,l in groupby(n)]
nnn=''
if n:
	for x,y in reversed(nn):
		nnn += x + (str(y) if y > 1 else "")
	print(nnn)
else:
	print('NONE')
'''8일차 3번 문제 (골드4급): 반복 그룹 압축 최적화

🔹 문제 설명

문자열을 입력받고, 연속된 문자 그룹을 다음과 같이 압축합니다:
	•	연속된 문자는 '문자+반복횟수'로 표현 (1회도 포함)
	•	단, 압축한 결과 문자열의 길이를 최소화하도록 한 번의 문자 교체 기회가 주어집니다.
	•	교체란, 문자열 내 한 문자를 다른 문자로 바꾸는 것을 의미합니다.
예: abbaaac에서 ‘b’ → ‘a’로 바꾸면 aaaaaac이 되고, 압축은 a6c1 (길이 4)

🔸 입력 형식
	•	소문자 알파벳으로 구성된 문자열 (1 ≤ 길이 ≤ 1000)

🔸 출력 형식
	•	교체를 한 번도 하지 않거나, 한 번만 했을 때 가능한 가장 짧은 압축 문자열의 길이'''
n = input().lower()
nn = [(st,len(list(l)))for st,l in groupby(n)]
nn
st = ''
change=True
print(nn)
for (x,y) in nn:
    st += x + str(y)
for ch in st:
    if change:
        if ch == 1:
            ind = st.index(ch)
            if ind != 1 and ind != len(str):
                if st[ind-3] == st[ind+1]:
                    st[ind-1] = st[ind-3]
                    change= False
            else:
                st[ind-1] 

print(st)

from itertools import groupby

def compress_length(s):
    return sum(len(k) + len(str(len(list(g)))) for k, g in groupby(s))
print(compress_length('aabbaaac'))
def best_compression(s):
    min_len = compress_length(s)
    for i in range(len(s)):
        for repl in 'abcdefghijklmnopqrstuvwxyz':
            if s[i] != repl:
                temp = s[:i] + repl + s[i+1:]
                min_len = min(min_len, compress_length(temp))
    return min_len

print(best_compression("aabbaaac"))  # 예시: 4
''' 문제 설명

문자열을 입력받고, 연속된 동일 문자 그룹을 다음 규칙에 따라 압축합니다:
	•	동일한 문자가 연속으로 등장하면 "문자+반복수" 형태로 압축합니다.
	•	단, 문자 그룹의 순서를 자유롭게 재정렬하여 압축 후 결과 문자열의 길이를 최소화해야 합니다.
	•	모든 그룹은 그대로 유지하되, 순서만 바꿀 수 있습니다.

예를 들어:
	•	입력: aabbcccaa
→ 그룹: aa, bb, ccc, aa
→ 중복 그룹을 먼저 합쳐서 정렬: aa + aa = aaaa, bb, ccc
→ aaaa → a4, bb → b2, ccc → c3
→ 출력: a4b2c3 (길이 6)

🔸 입력 형식
	•	한 줄의 문자열 (1 ≤ 길이 ≤ 1000), 소문자 알파벳만

🔸 출력 형식
	•	재정렬 후 압축된 문자열
	•	예시처럼 각 그룹마다 반드시 "문자+반복수" 형태로 출력 (1회도 포함: 예. a1)'''
n = input()
from collections import Counter
nn = Counter(n)
st = ''
for x,y in nn.items():
    st += x + str(y)
st

''' 8일차 5번 문제: 가장 긴 대칭 부분 문자열 찾기 (난이도: 실버 1)

🔹 문제 설명

문자열을 입력받아, 그 중 가장 긴 대칭(팰린드롬) 부분 문자열을 찾아 출력하세요.
	•	팰린드롬: 앞에서 읽어도, 뒤에서 읽어도 같은 문자열
	•	부분 문자열: 원래 문자열에서 연속된 일부 문자

⸻

🔸 입력 형식
	•	문자열 한 줄 (소문자 알파벳, 길이 ≤ 1000)

🔸 출력 형식
	•	가장 긴 팰린드롬 부분 문자열 (여러 개라면 앞에서 가장 먼저 나오는 것)

⸻
'''

def cor_pel(n):
    pel = []
    l = len(n)
    for i in range(l):
        for j in range(i + 1, l + 1):
            sub = n[i:j]
            if sub == sub[::-1] and len(sub)!=1:
                pel.append(sub) 
    pel = sorted(pel, key=lambda x: len(x),reverse=True)
    if pel:
        
    	return pel[0]
    else:
        print('none')
cor_pel('abacdfgdcaba')

                                
