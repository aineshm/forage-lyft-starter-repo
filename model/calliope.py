from datetime import datetime
from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery

class Calliope(Car):

    def __init__(self,last_service_date:datetime.date, current_mileage:int, last_service_mileage:int):
        super().__init__(SpindlerBattery(last_service_date),CapuletEngine(last_service_date, current_mileage, last_service_mileage))

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service
