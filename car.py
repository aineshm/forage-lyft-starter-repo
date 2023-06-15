from abc import ABC, abstractmethod
from serviceable import Serviceable
from engine import Engine
from battery import Battery

class Car(Serviceable):
    def __init__(self,engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        # if(self.engine.needs_service or self.battery.needs_service):
        #     return True
        # else:
        #     return False
        pass

