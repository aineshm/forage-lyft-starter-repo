from engine import Engine
from datetime import datetime

class WilloughbyEngine(Engine):
    def __init__(self, last_service_date:datetime, current_mileage:int, last_service_mileage:int):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 60000
