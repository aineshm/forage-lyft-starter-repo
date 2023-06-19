from datetime import datetime
from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class Palindrome(Car):
    def __init__(self,last_service_date:datetime, warning_light_is_on:bool,tire_type: str,tire_array):
         if tire_type.lower == "carrigan":
             super().__init__(SpindlerBattery(last_service_date),
                         SternmanEngine(last_service_date,warning_light_is_on),
                         Carrigan(tire_array))
         elif tire_type.lower == "octoprime":
             super().__init__(SpindlerBattery(last_service_date),
                         SternmanEngine(last_service_date,warning_light_is_on),
                         Octoprime(tire_array))
             

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service
    