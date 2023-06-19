from datetime import datetime
from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class Rorschach(Car):
    def __init__(self,last_service_date:datetime, current_mileage:int, last_service_mileage:int,tire_type: str,tire_array):
         if tire_type.lower == "carrigan":
             super().__init__(NubbinBattery(last_service_date),
                         WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                         Carrigan(tire_array))
         elif tire_type.lower == "octoprime":
             super().__init__(NubbinBattery(last_service_date),
                         WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                         Octoprime(tire_array))

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service or self.battery.needs_service
