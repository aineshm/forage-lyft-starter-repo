from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex
from datetime import date

class CarFactory():

    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type:str, tire_array):
        return Calliope(last_service_date, current_mileage, last_service_mileage,tire_type, tire_array)
    
    def create_glissade(last_service_date:date,current_mileage:int,last_service_mileage:int,tire_type:str, tire_array):
        return Glissade(last_service_date,current_mileage,last_service_mileage,tire_type, tire_array)
    
    def create_palindrome(last_service_date:date, warning_light_is_on:bool,tire_type:str, tire_array):
        return Palindrome(last_service_date, warning_light_is_on,tire_type,tire_array)
    
    def create_rorschach(last_service_date:date, current_mileage:int, last_service_mileage:int,tire_type:str, tire_array):
        return Rorschach(last_service_date, current_mileage, last_service_mileage,tire_type,tire_array)
    
    def create_thovex(last_service_date:date, current_mileage:int, last_service_mileage:int,tire_type:str, tire_array):
        return Thovex(last_service_date, current_mileage, last_service_mileage,tire_type,tire_array)