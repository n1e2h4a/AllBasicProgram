Number = int(input('Enter Number for prime Factorization:--'))
try:
    for Num in range(2, Number + 1):
        while Number % Num == 0:
            print(Num)
            Number = Number / Num
except ValueError:
    print("Try any other suitable number!")
