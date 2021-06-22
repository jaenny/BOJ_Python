# def solution(gems):
#     gems_set = set(gems)
#     answer = []
#     check = list(gems_set)
    
#     dp=[1000000 for x in range(len(gems))]
    
#     for i in range(len(gems)) :
#         dp[i] = []
#         flag = 0
#         for j in range(i,len(gems)) :
#             if gems[j] not in dp[i] :
#                 dp[i].append(gems[j])
#                 if len(dp[i]) == len(check) :
#                     dp[i] = j-i
#                     flag = 1
#                     break
#         if flag != 1 : 
#           dp[i] = 1000000
#           break
#         print(dp)
#     answer = [dp.index(min(dp))+1,dp.index(min(dp))+1+min(dp)]
#     return answer

def cal(start,end,gems):
  arr=gems[start:end+1]
  return set(arr)

def solution(gems):
    gems_set = set(gems)
    answer = []

    start = 0; end = 0
    flag = 0
    while True :
      if cal(start,end,gems) == gems_set :
        flag = 1
        start += 1
      else :
        if flag == 0 :
          end += 1
        else :
          answer = [start,end+1]
    return answer

print(solution(['a','b','b','c','b','a']))