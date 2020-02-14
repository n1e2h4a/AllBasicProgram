import random
Stake = int(input('How many stake do you have:--'))
Goal = int(input("what are the goals you want to achieve:--"))
win = 0
loss = 0
count = 0
while Stake >= 0:
    if Stake == Goal:
        break
    number = random.randint(0, 1)
    if number > .5:
        Stake = Stake+1
        win = win+1
        count = count+1
    else:
        Stake = Stake-1
        loss = loss+1
        count = count+1
WinPercent = round(win * 100 / count)
LossPercent = round(loss * 100 / count)

print("percentage of win {}".format (WinPercent))
print("percentage of loss {}".format (LossPercent))
