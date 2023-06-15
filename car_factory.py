from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class CarFactory():

    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        return Calliope(last_service_date, current_mileage, last_service_mileage)
    
    def create_glissade(last_service_date,current_mileage,last_service_mileage):
        return Glissade(last_service_date,current_mileage,last_service_mileage)
    
    def create_palindrome(last_service_date, warning_light_is_on):
        return Palindrome(last_service_date, warning_light_is_on)
    
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        return Rorschach(last_service_date, current_mileage, last_service_mileage)
    
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        return Thovex(last_service_date, current_mileage, last_service_mileage)