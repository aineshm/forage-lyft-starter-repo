from battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self,last_service_date:datetime):
        super().__init__(last_service_date)

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 4
