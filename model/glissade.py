from datetime import datetime
from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self,last_service_date):
        super().__init__(last_service_date,SpindlerBattery,WilloughbyEngine)

    def needs_service(self,current_date):
        return self.battery.needs_service or self.engine.needs_service
