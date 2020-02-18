class concate:
    def stringadd(self, number, newlist):
        result = " "
        if number > 0:
            for x in range(number):
                Element = input(' > ')
                newlist.append(Element)
            print(newlist)
            for strings in newlist:
                result += str(strings)
            return result


number = int(input("Enter number of digit for string you want to print:---"))

newlist = []
concatination = concate()
print(concatination.stringadd(number, newlist))
