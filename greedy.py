while True:
    cash = float(input("Cash:"))
    break

cash = cash * 100
final = 0
coin = [25, 10, 5, 1]

for i in range(4):
    while cash >= coin[i]:
        final = int((cash / coin[i]) + final)
        cash = cash % coin[i]

print(f"Amount of coins: {final}")