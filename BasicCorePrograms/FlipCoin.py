import random
Flip=int(input("Enter the number to flip the coin:--"))
head=0
tail = 0
try:
        if Flip>0:
            for Num in range(Flip):
                if random.random() > 0.5:
                    head=head+1
                else:
                    tail=tail+1
        print(f'Head count {0}',head)
        print(f'Tail count {0}',tail)
        Headpercent=head/Flip*1007

        Tailpercent=tail/Flip*100
        print(f'Head percentage {0}',Headpercent)
        print(f'Tail percentage {0}',Tailpercent)
except:
        print("Enter good input")


