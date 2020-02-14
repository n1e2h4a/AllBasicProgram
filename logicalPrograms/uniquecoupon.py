import random
CountOfCoupon = int(input('Enter the number of coupon you want:--'))
Rangein = int(input('Enter the range of coupon you want:--'))

Couponlist = []
for i in range(CountOfCoupon):
    coupon = random.randint(1, Rangein)
    if coupon not in Couponlist:
      Couponlist.append(coupon)
print(Couponlist)

