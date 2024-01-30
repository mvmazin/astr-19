#session 3 prompt ASTR_19

#Write a Python program that declares a class
#describing your favorite animal. Have the data members of the
#class represent the following physical parameters of the animal:
#length of the arms (float), length of the legs (float), number of eyes (int),
#does it have a tail? (bool), is it furry? (bool).
#Write an initialization function that sets the values of the data
#members when an instance of the class is created.
#Write a member function of the class to print out and describe the
#data members representing the physical characteristics of the animal.

class Emperor_Penguin:

    def __init__ (self, w, l, e, t,f):
        self.wing = w
        self.leg = l
        self.eyes = e
        self.tail = t
        self.fur = f

    def return_values(self):
        print("The wingspan of Emperor Penguins is:",float(self.wing),"centimeters.\nThe height of an Emperor Penguin is:",float(self.leg),"centimeters.\nThe Emperor Penguin has",int(self.eyes),"eyes.\nIt is",bool(self.tail),"that an Emperor Penguin has a tail. \nIt is",bool(self.fur),"that the Emperor Penguin has fur.")

if __name__=="__main__":

    penguin = Emperor_Penguin(77, 122, 2, 1, 0)
    penguin.return_values()

    

    
