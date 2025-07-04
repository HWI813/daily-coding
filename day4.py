'''1번 문제: 알파벳 빈도 분석기

문제 설명
사용자로부터 문자열을 입력받고, 각 알파벳(a-z)의 출현 횟수를 출력하시오.
대소문자는 구분하지 않고 소문자로 통일하여 계산합니다.
알파벳이 아닌 문자는 무시합니다.'''
word = input().lower().replace(' ','')
word = ''.join([ch for ch in word if ch.isalpha()])
from collections import Counter
alpha=(Counter(word))
al = sorted(alpha.items())
for key, val in al:
    
    print(f'{key} : {val}')
    
'''
2번 문제: 단어의 모음 비율 정렬

🔹 문제 설명

여러 개의 단어를 입력받은 뒤, 각 단어의 모음(a, e, i, o, u) 비율을 계산하고,
모음 비율이 높은 순서로 정렬하여 출력하시오.
단, 모음 비율이 같다면 사전순으로 정렬하세요.

🔹 입력 형식
	•	첫 줄에 단어의 개수 N이 주어집니다.
	•	이후 N줄에 걸쳐 알파벳 소문자로 된 단어들이 주어집니다.

🔹 출력 형식
	•	모음 비율이 높은 단어부터 출력 (비율은 계산만 하고 출력하지 않아도 됩니다)
'''

n = int(input())

word = {}
for _ in range(n):
    h = input()
    word[h] = ((sum(1 for j in h if j in 'aeiou')) /len(h) )
n_word = sorted(word.items(), key=lambda x: (-x[1],x[0]))
for k,_ in n_word:
    print(k)


'''3번 문제: 단어 내 숫자 합산기

🔹 문제 설명
문자열 안에 포함된 모든 숫자를 찾아 합을 구하는 프로그램을 작성하세요.
문자열은 알파벳과 숫자가 섞여 있으며, 숫자는 연속된 숫자일 수도 있습니다.

🔹 입력 형식
	•	문자열 한 줄이 주어집니다. (예: abc12def34gh5)

🔹 출력 형식
	•	문자열 내에 포함된 모든 숫자의 합을 출력합니다.
(위 예시의 경우 12 + 34 + 5 = 51)'''
word = input() 
n_w = []
for i in range(len(word)):
    if word[i:i+2].isdigit():
        n_w.append(word[i:i+2])
    else:
        if word[i-1:i+1].isdigit():
           pass
        elif word[i].isdigit():
           n_w.append(word[i]) 
duha = 0
for s in n_w:
    duha += int(s)
duha

import re
text = input()
num = re.findall(r'\d+',text)
print(sum(map(int,num)))

text = input()
num = ''
total = 0
for i in text:
    if i.isdigit():
        num+=i
    else:
        if num:
            total += int(num)
            num=''
if num:
    total += int(num)
total

''' 4번 문제: 단어 회전 비교기

🔹 문제 설명
단어를 입력받고, 그 단어를 왼쪽으로 한 글자씩 회전시킨 모든 경우를 출력하세요.
단, 회전 결과가 원래 단어와 동일해지는 경우가 있다면, 그 시점을 알려주세요.

⸻

🔹 입력 형식
	•	문자열 한 줄 (소문자 알파벳으로 구성, 길이 2 이상)

🔹 출력 형식
	•	회전된 단어들을 한 줄에 하나씩 출력
	•	만약 회전 중 원래 단어와 같아지는 경우가 있다면,
"원래 단어와 같아짐: X회전" 을 마지막 줄에 출력
(0회전은 제외)'''

word = input()
text = word
for i in range(1,len(word)+1):
    text = text[1:]+text[0]
    if text == word:
        print(f'원래 단어와 같아짐 : {i}회전')
        break
    else:
        print(text)