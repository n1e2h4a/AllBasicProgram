
score = {'rank1':[1,2,3],'rank2':[5,6,7],'rank3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(score.items()))):
    print(*row)

