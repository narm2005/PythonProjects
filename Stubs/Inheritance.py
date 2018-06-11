# parent class
class Bird:
    
    def __init__(self):
        self.__color='Red';
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Robin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("color".format(self.__color))
        print("Robin is ready")

    def whoisThis(self):
        print("Robin")

    def run(self):
        print("Run faster")

peggy = Robin()
peggy.whoisThis()
peggy.swim()
peggy.run()

bird=Bird()
bird.swim()
#bird.run()
