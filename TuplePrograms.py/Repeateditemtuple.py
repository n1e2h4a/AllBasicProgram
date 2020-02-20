top = ("nine", "2", "o", "o", "8.9")

choice = input("Enter the choice:--")
for x in top:
    if choice == x:
        print(f'the repeated element {choice} is {top.count(x)}')
        break
