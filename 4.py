def solution(n, start, end, roads, traps):
    from collections import deque
    answer = []
    avail=deque()
    for r in roads :
      if r[0] == start : 
        avail.append(r+[0])
    now = start
    print("avail : ",avail)

    flag = 0
    while avail :
      s,e,t,res = avail.popleft()
      print('------------------------------')
      print(s,e,t,res)
      now = e
      
      #종료조건
      if now == end :
        if t+res not in answer :
          answer.append(t+res)
          if len(answer) > 1 :
            if (t+res) % min(answer) == 0 : return min(answer)

      #trap에서 경로 바꾸기
      if now in traps :
        for i in range(len(roads)) :
          if roads[i][0] == now or roads[i][1] == now :
            roads[i] = [roads[i][1],roads[i][0],roads[i][2]]
        print("after traps :",roads)
      for r in roads :
        if r[0] == now :
          avail.append(r+[t+res])
      print("avail:",avail)
    return min(answer)