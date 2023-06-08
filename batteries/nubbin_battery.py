from battery import Battery
from datetime import date

class NubbinBattery(Battery):
    def __init__(self,last_service_date:date):
        super.__init__(last_service_date)

    def needs_service(self):
        return self.current_date - self.last_service_date.year < 4
