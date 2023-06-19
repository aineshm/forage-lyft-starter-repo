from serviceable import Serviceable

class Tire(Serviceable):

    def __init__(self,tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        pass