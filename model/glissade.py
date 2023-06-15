from datetime import datetime
from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self,last_service_date:datetime, current_mileage:int, last_service_mileage:int):
        super().__init__(SpindlerBattery(last_service_date),
                         WilloughbyEngine(last_service_date,current_mileage,last_service_mileage))

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service
