from engine import Engine
from datetime import datetime

class SternmanEngine(Engine):
    def __init__(self, last_service_date:datetime, warning_light_is_on:bool):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
