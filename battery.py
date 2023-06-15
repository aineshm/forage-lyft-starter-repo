from serviceable import Serviceable
from datetime import datetime

class Battery(Serviceable):

    def __init__(self,last_service_date:datetime):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self):
        pass