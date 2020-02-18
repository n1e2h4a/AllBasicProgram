class sort:
    def sorting(self, number, newlist):
        if number > 0:
            # enter the number for number of element you want to take in list
            for x in range(number):
                # input in list
                Element = int((input(' > ')))
                # empty list appended by the input
                newlist.append(Element)
            # if check(digretit which you want
            newlist.sort()
            return print(newlist)
            # return newlist.sort()


number = int(input("Enter number of digit you want to print:---"))
newlist = []
num = sort()
num.sorting(number, newlist)
