n = int(input())
change = 1000 - n

coins = [500,100,50,10,5,1]

cnt = 0

for coin in coins :
  if change // coin > 0 :
    cnt += change // coin
    change = change % coin

print(cnt)