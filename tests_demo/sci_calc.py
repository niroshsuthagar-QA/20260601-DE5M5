from calc import Calculator

class Sci_calc(Calculator):
    
    def exp(self):
        return self.num1**self.num2
    

myNewCal = Sci_calc(10,2)

print(myNewCal.exp())