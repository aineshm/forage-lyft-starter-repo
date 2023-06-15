from datetime import datetime
from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery

class Thovex(Car):
    def __init__(self,last_service_date:datetime, current_mileage:int, last_service_mileage:int):
        super().__init__(NubbinBattery(last_service_date),CapuletEngine(last_service_date, current_mileage, last_service_mileage))

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service
