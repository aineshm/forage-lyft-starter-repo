from datetime import datetime
from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery

class Thovex(Car):
    def __init__(self,last_service_date):
        super().__init__(last_service_date,NubbinBattery,CapuletEngine)

    def needs_service(self,current_date):
        return self.battery.needs_service or self.engine.needs_service
