cash = -1
while cash < 0:
    cash = float(input("Cash:"))
    break

final = 0
coin = [.25, .10, .05, .01]

for i in range(4):
    while cash >= coin[i]:
        final = int((cash / coin[i]) + final)
        cash = cash % coin[i]

print(f"Amount of coins: {final}")