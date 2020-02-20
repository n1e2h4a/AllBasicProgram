Grade = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(Grade)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
Grade = Grade[:2] + Grade[3:]
print(Grade)
#converting the tuple to list
rank = list(Grade)
#use different ways to remove an item of the list
rank.remove("c") 
#converting the tuple to list
Grade = tuple(rank)
print(Grade)
