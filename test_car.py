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

    def test_spindler_battery_exactly_2_years(self):
        last_service_date = datetime(2021,6,11)
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

# class TestCalliope(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
