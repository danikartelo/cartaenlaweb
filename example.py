# Python program to
# demonstrate private methods

# Creating a class
class A:

    # Declaring public method
    def fun(self):
        print("Public method")

    # Declaring private method
    def __fun(self):
        print("Private method")

    # Calling private method via
    # another method
    def Help(self):
        self.fun()
        self.__fun()

# Driver's code
obj = A()
obj.__fun()
obj.Help() 
