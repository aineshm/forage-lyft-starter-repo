from datetime import datetime
from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self,last_service_date:datetime, warning_light_is_on:bool):
        super().__init__(SpindlerBattery(last_service_date),
                         SternmanEngine(last_service_date,warning_light_is_on))

    def needs_service(self):
        return self.battery.needs_service or self.engine.needs_service
    