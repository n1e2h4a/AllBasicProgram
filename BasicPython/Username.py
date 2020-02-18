class Name:
    def username(self, Firstname, Lastname):
        Fullname = Firstname + " " + Lastname
        print("My Fullname is", Fullname)
        return print(f'My Reverse name is {Lastname} {Firstname}')

Firstname = input("Enter the Firstname:--")
Lastname = input("Enter the lastname:--")
Myname = Name()
Myname.username(Firstname, Lastname)
