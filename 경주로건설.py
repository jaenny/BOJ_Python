from collections import deque
import sys
def solution(board):
  cost = [[sys.maxsize]*len(board[0]) for i in range(len(board[0]))]
  direction = [[1,0],[0,1],[-1,0],[0,-1]]
  answer = sys.maxsize
  queue=deque()
  queue.append([0,0,0,-1]) #i,j,cost,dir
  cost[0][0]=0

  while queue :
    i,j,Pay,Dir = queue.popleft()

    if i == len(board[0])-1 and j == len(board[0])-1 :
      answer = min(answer,cost[i][j])
      continue
    
    for d in direction :
      di = i + d[0]
      dj = j + d[1]
      if 0<=di<len(board[0]) and 0<=dj<len(board[0]) and board[di][dj] != 1:
        if Dir == -1 or Dir == d :
          nPay = Pay + 100
        else :
          nPay = Pay + 600
        
        if cost[di][dj] >= nPay :
          cost[di][dj] = nPay
          queue.append([di,dj,nPay,d])
  return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))