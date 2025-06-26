# ----------------------------
# Day 2
# ----------------------------

# 문제 1. 최댓값

num = []
for _ in range(9):
    n = int(input())
    num.append(n)
max_num = max(num)
print(max_num,num.index(max_num)+1)

# 문제 2. 점수 조정
n = int(input())
a = list(map(int,input().split(' ')))
max_n = max(a)
nw_a = []
new_a = [x / max_n * 100 for x in a]
print(f'{sum(nw_a):.2f}')
# 문제 3. 문자 개수 세기
st = input()
s = input()
print(st.count(s))

# 문제 4. 평균 넘는 학생 비율
nums = list(map(int, input().split()))
if len(nums) <= 1:
    pass
else:
    aver = sum(nums) / (len(nums) )
    n_nums = [x for x in nums if x > aver]
    print(f'{(len(n_nums)/ len(nums))*100:.2f}%')


'''입력: 문자열 하나
출력: 가장 많이 등장한 알파벳 (여러 개면 ? 출력)
예시:
  입력: Mississipi
  출력: ?
  입력: zZa
  출력: Z
'''
from collections import Counter
st = input('입력 : ').upper()
c=Counter(st)

aa=c.most_common(2)
if aa[0][1] == aa[1][1]:
    print('출력 : ?')
else:
    print('출력 :',aa[0][0])

'''
입력: 첫 줄에 테스트케이스 수 N
     다음 N줄에 "학생 수 + 점수들" 형태 입력
출력: 각 줄마다 "평균보다 높은 학생 비율"을 퍼센트로 %.3f형식으로 출력

예시 입력:
2
5 50 50 70 80 100
7 100 95 90 80 70 60 50

예시 출력:
40.000%
57.143%'''
N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))
    n = a[0] 
    a = a[1:]
    aver = sum(a)/n
    n_a = [x for x in a if x > aver]
    print(f'{len(n_a)/n*100:.3f,}%')

'''입력: N개의 단어
출력: 중복 제거 후, 길이순 정렬 → 길이 같으면 사전순 정렬

예시 입력:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

예시 출력:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate'''
n = int(input())
ss = set()
for _ in range(n):
    st = input()
    ss.add(st)
print(sorted(ss))