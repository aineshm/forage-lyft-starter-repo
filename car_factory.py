from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class CarFactory():

    def create_calliope(last_service_date):
        return Calliope(last_service_date)
    
    def create_glissade(last_service_date):
        return Glissade(last_service_date)
    
    def create_palindrome(last_service_date):
        return Palindrome(last_service_date)
    
    def create_rorschach(last_service_date):
        return Rorschach(last_service_date)
    
    def create_thovex(last_service_date):
        return Thovex(last_service_date)