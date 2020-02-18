class checknum:
    def checkk(self, number, check, newlist):
        if number > 0:
            # enter the number for number of element you want to take in list
            for x in range(number):
                # input in list
                Element = int((input(' > ')))
                # empty list appended by the input
                newlist.append(Element)
        # if check(digit which you want to check) in list print true else false
        if check in newlist:
            return True
        else:
            return False


try:
    # inputs
    number = int(input("Enter number of digit you want to print:---"))
    check = int(input("Enter the element which you want to check in list"))
    newlist = []
    result = checknum()
    print(result.checkk(number, check, newlist))
except:
    print("result not found")
