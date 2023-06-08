from serviceable import Serviceable
from datetime import date

class Battery(Serviceable):

    def __init__(self,last_service_date:date):
        self.last_service_date = last_service_date
        self.current_date = date.today

    def needs_service(self):
        pass