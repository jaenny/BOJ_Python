# 입력
n = int(input())
time = []
for i in range(n) :
  start, end = map(int,input().split())
  time.append([start,end])

# 정렬하기
# 1. 먼저 끝나는 순서대로 정렬 -> 그래야 뒤에 뭐라도 더 오지
# 2. 먼저 시작하는 순서대로 정렬 -> (2,2),(1,2) 라면 (1,2),(2,2) 순서로 되도록
time.sort(key=lambda x : (x[1],x[0]))

cnt = 0
end_time = 0

for t in time :
  if t[0] >= end_time :
    end_time = t[1]
    cnt += 1

print(cnt)