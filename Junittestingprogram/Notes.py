Amount = int(input('Enter the amount you want to take:-'))
Notes = [1000, 500, 100, 50, 10, 5, 2, 1]
NoteCount = [0, 0, 0, 0, 0, 0, 0, 0]
print("count of your notes")
for i, j in zip(Notes, NoteCount):
    if Amount >= i:
        j = Amount//i
        Amount = Amount-j*i
        print(i, " : ", j)
