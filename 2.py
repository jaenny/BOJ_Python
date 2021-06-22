def bfs(k,i,j,places,visit) :
  visit[i][j] = 1

  #1 : places[k][i][j]를 둘러싼 8개 확인
  d8 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
  for d in d8 :
    di = i + d[0]
    dj = j + d[1]
    if 0<=di<5 and 0<=dj<5 and visit[di][dj] == 0 :
      visit[di][dj] = 1
      if places[k][di][dj] == 'P' :
        if d == [-1,-1] : 
          if places[k][di][dj+1] == 'X' and places[k][di+1][dj] == 'X' : continue
          else : return 0
        elif d == [-1,1] : 
          if places[k][di][dj-1] == 'X' and places[k][di+1][dj] == 'X' : continue
          else : return 0
        elif d == [1,1] : 
          if places[k][di-1][dj] == 'X' and places[k][di][dj-1] == 'X' : continue
          else : return 0
        elif d == [1,-1] : 
          if places[k][di-1][dj] == 'X' and places[k][di][dj+1] == 'X' : continue
          else : return 0
        return 0
  for h in range(5) :
    print(visit[h])
  print('')

  #2 : places[k][i][j]에서 직선 맨허튼 거리 2를 가지는 4개 확인
  d4 = [[2,0],[0,2],[-2,0],[0,-2]]
  for d in d4 :
    di = i + d[0]
    dj = j + d[1]
    if 0<=di<5 and 0<=dj<5 and visit[di][dj] == 0 :
      visit[di][dj] = 1
      if places[k][di][dj] == 'P' :
        if d == [-2,0] :
          if places[k][di+1][dj] == 'X' : continue 
          else : return 0
        elif d == [0,2] :
          if places[k][di][dj-1] == 'X' : continue 
          else : return 0
        elif d == [2,0] :
          if places[k][di-1][dj] == 'X' : continue 
          else : return 0
        elif d == [0,-2] :
          if places[k][di][dj+1] == 'X' : continue 
          else : return 0

  for h in range(5) :
    print(visit[h])
  print('--------')

  return 1


def solution(places):
    answer = [1,1,1,1,1] # 1:거리두기 지킴 / 0:거리두기 안지킴

    for k in range(5) : #room 하나씩
      flag = 0
      print('***************')
      visit = [[0,0,0,0,0] for x in range(5)]
      for i in range(5) :
        for j in range(5) :
          if places[k][i][j] == 'P' :
            if bfs(k,i,j,places,visit) == 0 : 
              flag = 1
              answer[k] = 0
              print(k,answer)
              break
        if flag == 1 : break

    return answer

print("a",solution([["XXXOX", "OXXXX", "OOXOX", "XXXOP", "OXXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))