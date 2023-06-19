from tire import Tire

class Carrigan (Tire):
    def __init__(self, tire_array):
        super().__init__(tire_array)
    
    def needs_service(self):
        for i in self.tire_array:
            if(i>=0.9):
                return True
        return False
    