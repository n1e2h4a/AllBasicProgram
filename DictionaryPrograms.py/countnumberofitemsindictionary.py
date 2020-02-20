def main():
    grade= {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9,8,4,7],
         'B': 34,
         'C': 12,
         'D': [7, 8, 9, 6, 4]}
    count=0
    for x in grade:
        if isinstance(grade[x], list):
            count+=len(grade[x])
    print(count)
    #calling main
if __name__ == "__main__":
    main()