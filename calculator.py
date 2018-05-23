

class Calculator():

    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """
    @staticmethod
    def add(arg1, arg2):
      return arg1 + arg2
    @staticmethod
    def subtract(arg1,arg2):
      return arg1 - arg2
    @staticmethod
    def multiply(arg1,arg2):
      return arg1 * arg2
    @staticmethod
    def divide(arg1,arg2):
      return arg1 / arg2

 
calculate = Calculator()
print(calculate.subtract(3,4))