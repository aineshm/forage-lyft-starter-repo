import unittest
from datetime import datetime
from battery import Battery
from engine import Engine
from car_factory import CarFactory
from car import Car

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tire import Tire
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

# from model.calliope import Calliope
# from model.glissade import Glissade
# from model.palindrome import Palindrome
# from model.rorschach import Rorschach
# from model.thovex import Thovex

class TestBatteries(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        last_service_date = datetime(2009,11,13)
        battery1 = NubbinBattery(last_service_date)
        self.assertTrue(battery1.needs_service())

    def test_nubbin_battery_no_need_service(self):
        last_service_date = datetime(2022,11,13)
        battery1 = NubbinBattery(last_service_date)
        self.assertFalse(battery1.needs_service())

    def test_nubbin_battery_exactly_4_years(self):
        last_service_date = datetime(2019,6,11)
        battery1 = NubbinBattery(last_service_date)
        self.assertTrue(battery1)

    def test_spindler_battery_needs_service(self):
        last_service_date = datetime(2009,11,13)
        battery1 = SpindlerBattery(last_service_date)
        self.assertTrue(battery1.needs_service())

    def test_spindler_battery_no_need_service(self):
        last_service_date = datetime(2023,3,13)
        battery1 = SpindlerBattery(last_service_date)
        self.assertFalse(battery1.needs_service())

    def test_spindler_battery_exactly_3_years(self):
        last_service_date = datetime(2020,6,11)
        battery1 = SpindlerBattery(last_service_date)
        self.assertTrue(battery1.needs_service())

class TestEngines(unittest.TestCase):
    def test_capulet_needs_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = CapuletEngine(last_service_date,45000,10000)
        self.assertTrue(engine1.needs_service()) 
         
    def test_capulet_no_need_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = CapuletEngine(last_service_date,45000,16000)
        self.assertFalse(engine1.needs_service()) 

    def test_sternman_needs_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = SternmanEngine(last_service_date,True)
        self.assertTrue(engine1.needs_service())

    def test_sternman_no_need_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = SternmanEngine(last_service_date,False)
        self.assertFalse(engine1.needs_service())

    def test_willoughby_needs_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = WilloughbyEngine(last_service_date,60001,0)
        self.assertTrue(engine1.needs_service())

    def test_willoughby_no_need_service(self):
        last_service_date = datetime(2021,6,11)
        engine1 = WilloughbyEngine(last_service_date,50000,0)
        self.assertFalse(engine1.needs_service())

class TestTires(unittest.TestCase):
    def test_carrigan_needs_service(self):
        tire_array = [0.1, 0.4, 0.9, 0.8]
        tire1 = Carrigan(tire_array)
        self.assertTrue(tire1.needs_service())

    def test_carrigan_no_need_service(self):
        tire_array = [0.1, 0.4, 0.3, 0.8]
        tire1 = Carrigan(tire_array)
        self.assertFalse(tire1.needs_service())

    def test_carrigan_no_need_service1(self):
        tire_array = [0.8, 0.8, 0.8, 0.8]
        tire1 = Carrigan(tire_array)
        self.assertFalse(tire1.needs_service())

    def test_octoprime_needs_service(self):
        tire_array = [0.1,1,0.9,1]
        tire1 = Octoprime(tire_array)
        self.assertTrue(tire1.needs_service())

    def test_octoprime_needs_service1(self):
        tire_array = [0.8,0.8,0.8,0.8]
        tire1 = Octoprime(tire_array)
        self.assertTrue(tire1.needs_service())

    def test_octoprime_no_need_service(self):
        tire_array = [0.1,0.2,0.3,0.9]
        tire1 = Octoprime(tire_array)
        self.assertFalse(tire1.needs_service())

    def test_octoprime_no_need_service1(self):
        tire_array = [0.1,1,0.9,0.9]
        tire1 = Octoprime(tire_array)
        self.assertFalse(tire1.needs_service())
        
    


if __name__ == '__main__':
    unittest.main()
