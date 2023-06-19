from tire import Tire

class Octoprime(Tire):
    def __init__(self, tire_array):
        super().__init__(tire_array)

    def needs_service(self):
        sum = float(0)
        for i in self.tire_array:
            sum += i
        if(sum>=3):
            return True
        return False
