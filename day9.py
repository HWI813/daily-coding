''' 9일차 1번 리뉴얼 문제: 부분 회문 판별자

🔹 문제 설명
문자열이 주어졌을 때, 단 한 글자만 삭제하면 회문(Palindrome) 이 되는지 판단하는 프로그램을 작성하세요.
(단, 처음부터 회문이면 “0”, 한 글자만 지워서 회문이 되면 “1”, 어떤 경우도 아니면 “2”를 출력)

🔹 입력 형식
	•	문자열 한 줄 (길이 1 이상 1000 이하, 영소문자)

🔹 출력 형식
	•	0, 1, 2 중 하나를 출력
'''

def chance_pal(word):
    if word[::] == word[::-1]:
            return 0
    for i in range(len(word)):
        tem = word[:i]+ word[i+1:]
        if tem[::] == tem[::-1]:
            return 1
    return 2

    
word = input()
print(chance_pal(word))


'''문제 설명

소문자로 구성된 문자열이 주어졌을 때,
중복된 문자가 없는 가장 긴 부분 문자열의 길이를 출력하세요.

예를 들어 "abcabcbb"의 경우 "abc"가 가장 길며, 길이는 3입니다.

🔸 입력 형식
	•	영문 소문자 문자열 (1 ≤ 길이 ≤ 1000)

🔸 출력 형식
	•	중복 없이 연속되는 가장 긴 부분 문자열의 길이 (정수 하나)'''
n = input()
def fin_no(n):
    sen = {}
    left = 0
    max_l = 0
    for right in range(len(n)):
        if n[right] in sen and sen[n[right]] >= left:
            left = sen[n[right]] + 1
        sen[n[right]] = right
        max_l = max(max_l, right-left+1)
    return max_l
print(fin_no(n))
    
'''9일차 3번 문제: 알파벳 재배열로 가장 큰 수 만들기 (난이도: 실버 2 ~ 골드 5)

🔹 문제 설명

알파벳과 숫자가 섞인 문자열이 주어집니다.
	•	숫자만 모두 추출해서 합을 계산하고,
	•	**알파벳은 사전 역순(내림차순)**으로 정렬하여 이어붙이세요.
	•	마지막에 숫자 합을 문자열 뒤에 이어붙이세요.

단, 숫자가 없으면 숫자 합은 0으로 처리하세요.

⸻

🔸 입력 형식
	•	길이 1 이상 1000 이하의 문자열 (알파벳 소문자 + 숫자)

🔸 출력 형식
	•	사전 역순 정렬된 알파벳 + 숫자합 (문자열 형태)'''
import re
def re_batch(s):
    al = sorted([x for x in s if x.isalpha()], reverse=True)
    num = re.findall(r'\d+',s)
    if num:
        to = sum(map(int,num))
        return ''.join(al)+str(to)
    else:
        return ''.join(al)+str(0)


n = input()
print(re_batch(n))

'''9일차 4번 문제: 가장 긴 연속 숫자 구간 찾기 (난이도: 실버1~골드5 수준)

🔹 문제 설명

영문자와 숫자가 섞인 문자열이 주어졌을 때, 연속된 숫자들의 구간 중 가장 긴 숫자 문자열을 출력하세요.

여러 개일 경우, 가장 앞에 나오는 것을 출력합니다.

⸻

🔸 입력 형식
	•	영문자와 숫자로 이루어진 문자열 (길이 ≤ 1000)

⸻

🔸 출력 형식
	•	가장 긴 연속 숫자 문자열 1개 출력'''
n = input()
num = re.findall(r'\d+',n)
num = sorted(num, key=lambda x: len(x),reverse=True)
if num:

    print((num[0]))
else:
    print('NONE')

'''9일차 5번 문제: 서로 다른 문자 K개 포함한 가장 짧은 부분 문자열

🔹 문제 설명

문자열이 주어졌을 때,
서로 다른 문자 종류가 정확히 K개 포함된 가장 짧은 연속 부분 문자열의 길이를 구하세요.
만약 그런 부분 문자열이 없다면 “0”을 출력하세요.

⸻

🔸 입력 형식
	•	문자열 한 줄 (1 ≤ 길이 ≤ 1,000)
	•	다음 줄에 정수 K (1 ≤ K ≤ 26)

⸻

🔸 출력 형식
	•	조건을 만족하는 가장 짧은 부분 문자열의 길이 (정수)
	•	없으면 0 출력
'''
from collections import Counter
def short_l(s, k):
    left = 0
    count = {}
    min_len = float('inf')

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        # 조건을 만족할 때까지 윈도우 줄이기
        while len(count) >= k:
            if len(count) == k:
                min_len = min(min_len, right - left + 1)

            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

    return min_len if min_len != float('inf') else 0

n= input()
k = int(input())
print(short_l(n,k))
