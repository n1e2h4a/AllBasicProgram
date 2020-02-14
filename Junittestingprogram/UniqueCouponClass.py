import random
class coupon:

    def uniquecoupon(self,CountOfCoupon,Rangein):
        Couponlist = []
        for i in range(CountOfCoupon):
            coupon = random.randrange(1, Rangein)
            if coupon not in Couponlist:
              Couponlist.append(coupon)
        print(Couponlist)

CountOfCoupon = int(input('Enter the number of coupon you want:--'))
Rangein = int(input('Enter the range of coupon you want:--'))
numbers=coupon()
numbers.uniquecoupon(CountOfCoupon,Rangein)
