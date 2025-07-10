'''10일차 1번 문제: K번째로 큰 수 만들기 (난이도: 실버 1)

🔹 문제 설명
서로 다른 N개의 자연수가 주어질 때, 이 중 세 수를 더해 만들 수 있는 모든 합 중에서 K번째로 큰 수를 출력하는 프로그램을 작성하세요.

🔸 입력 형식
	•	첫 번째 줄에 자연수 N(3 ≤ N ≤ 100)과 K(1 ≤ K ≤ 50)가 주어집니다.
	•	두 번째 줄에 N개의 서로 다른 자연수가 공백을 사이에 두고 주어집니다.

🔸 출력 형식
	•	가능한 합 중 K번째로 큰 수를 출력합니다.
	•	불가능한 경우는 -1을 출력합니다.'''

from itertools import combinations

def thr_add(nums,k):
    add_list = set()
    com = combinations(nums,3)
    for comb in com:
        add_list.add(sum(comb))
    sorted_num = sorted(add_list, reverse=True)
    if len(nums)<=2:
        return -1
    else:
        return sorted_num[k-1]
n, k = map(int, input().split())
nums = list(map(int,input().split()))
print(thr_add(nums,k))

'''10일차 2번 문제: 숫자 배열 내에서 특정 합을 만드는 쌍 찾기 (난이도: 실버 2~골드 5급)

⸻

🔹 문제 설명

정수 배열이 주어졌을 때, 배열 내에서 서로 다른 두 수를 골라 합이 특정 값이 되는 **쌍(pair)**의 개수를 구하세요.

⸻

🔸 입력 형식
	•	첫째 줄: 정수 N (2 ≤ N ≤ 10,000) — 배열의 길이
	•	둘째 줄: N개의 정수 (각각은 -100,000 이상 100,000 이하)
	•	셋째 줄: 정수 K — 목표 합

⸻

🔸 출력 형식
	•	합이 K가 되는 서로 다른 두 수의 쌍의 개수 (중복 쌍은 1개로 셉니다)'''
from itertools import combinations

def find_k(num,k):
    com = combinations(num,2)
    sum_li= list()
    for c in com:
        if sum(c) == k:
            sum_li.append(sum(c))
    return len(sum_li)
n = int(input())
num = list(map(int, input().split()))
k = int(input())
print(find_k(num,k))
def find_k(num,k):
    s = []
    cnt = 0
    for i in num:
        target = k - x 
        if target:
            s.append(target)
    return s
n = int(input())
num = list(map(int, input().split()))
k = int(input())
print(find_k(num,k))
        

'''10일차 3번 문제: 슬라이딩 윈도우 최대값

🔹 문제 설명

정수로 이루어진 리스트 nums가 주어질 때, 고정된 크기 k의 윈도우를 오른쪽으로 하나씩 이동시키며, 각 윈도우에서 최댓값을 구하는 프로그램을 작성하세요.

⸻

🔸 입력 형식
	•	첫 줄에 정수 N과 K가 주어짐 (1 ≤ K ≤ N ≤ 10⁵)
	•	둘째 줄에 N개의 정수로 구성된 리스트 nums가 공백으로 구분되어 주어짐 (각 수는 -10⁴ 이상 10⁴ 이하)

⸻

🔸 출력 형식
	•	윈도우가 이동할 때마다 해당 윈도우의 최댓값을 한 줄로 출력 (공백으로 구분)'''
n,k = map(int, input().split())
nums = list(map(int, input().split()))
from collections import deque
import heapq
def shift_num(nums, k):
    ss = deque()
    max_sum = 0
    window_sum = 0
    for i in range(len(nums)):
        ss.append(nums[i])
        window_sum += nums[i]
        if len(ss) > k:
            window_sum -= ss.popleft()
        if len(ss) == k:
            max_sum = max(max_sum, window_sum)
    return max_sum
shift_num(nums,k)
    
'''🧠 10일차 4번 문제: 윈도우 이동 최대값 (난이도: 골드4)

🔹 문제 설명

정수로 이루어진 수열이 주어졌을 때, 길이 k인 윈도우를 왼쪽에서 오른쪽으로 한 칸씩 이동하며, 각 윈도우 내에서의 최댓값을 출력하는 프로그램을 작성하세요.

🔸 입력 형식
	•	첫째 줄: 정수 n과 k가 공백으로 구분되어 주어짐 (1 ≤ k ≤ n ≤ 100,000)
	•	둘째 줄: 공백으로 구분된 n개의 정수 (−1,000,000 ≤ 정수 ≤ 1,000,000)

🔸 출력 형식
	•	윈도우가 이동할 때마다의 최댓값들을 공백으로 출력'''
n,k = map(int, input().split())
nums = list(map(int, input().split()))
from collections import deque
def win_max(nums, k):

    n_n = deque(nums)
    for _ in range(len(nums)-k+1):
        print(max(list(n_n)[:k]), end= ' ')
        nums = n_n.popleft()
        

win_max(nums, k)

'''10일차 5번 문제: 최소 윈도우 서브스트링

🔹 문제 설명

문자열 s와 문자열 t가 주어집니다. s 안에서 t의 모든 문자를 포함하는 가장 짧은 부분 문자열을 구하세요.
	•	단, t에 같은 문자가 여러 개 있다면 그 개수도 만족해야 합니다.
	•	그런 부분 문자열이 없다면 "NONE"을 출력합니다.

🔸 입력 형식
	•	첫 줄: 문자열 s (1 ≤ len(s) ≤ 1000)
	•	두 번째 줄: 문자열 t (1 ≤ len(t) ≤ 1000)

🔸 출력 형식
	•	가장 짧은 부분 문자열. 없으면 "NONE"'''
from collections import Counter
s = input().strip()
t = input().strip()
need = Counter(t)
have = Counter()
left = 0
min_len = float('inf')
answer = ""
match = 0

for right in range(len(s)):
    have[s[right]] += 1
    while all(have[c] >= need[c] for c in need):
        if right - left + 1 < min_len:
            min_len = right - left + 1
            answer = s[left:right+1]
        have[s[left]] -= 1
        left += 1

if answer:
    print(answer)
else:
    print("NONE")

    