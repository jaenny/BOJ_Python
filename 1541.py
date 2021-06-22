ex = input()

flag = 0 # -가 나왔나요?
for i in range(len(ex)) :
  if ex[i] == '-' :
    flag = 1
  if flag == 1 and ex[i] == '+' :
    ex = ex[:i]+'-'+ex[i+1:]

res = 0

if '+' in ex :
  ex = ex.split('+')
  temp = list(map(int,ex[-1].split('-')))

  for i in range(len(ex)-1) :
    res += int(ex[i])
  
  res += (-1)*sum(temp)
  res += 2*temp[0]
  print(res)

else :
  ex = list(map(int,ex.split('-')))
  temp = sum(ex[1:])*(-1)
  res = ex[0] + temp
  print(res)
