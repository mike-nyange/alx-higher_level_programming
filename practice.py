class Sum:
    @staticmethod
    def getSum(*args):
        sum = 0 
        for i in args:
            sum += i
        return sum
    
class Dog:
    num_of_dogs = 0
    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs +=1
        
    @staticmethod
    def getNumberOfDogs():
        print(f'There are currently {Dog.num_of_dogs} dogs')
    
def main():
    #print("Sum :", Sum.getSum(1,2,3,4,5))
    spot = Dog("Spot")
    doug = Dog("Doug")
    men = Dog("Men")
    Dog.getNumberOfDogs()
    
    
    
main()
