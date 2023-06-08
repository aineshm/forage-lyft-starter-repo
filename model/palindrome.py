from datetime import datetime
from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self,last_service_date):
        super().__init__(last_service_date,SpindlerBattery,SternmanEngine)

    def needs_service(self,current_date):
        return self.battery.needs_service or self.engine.needs_service
