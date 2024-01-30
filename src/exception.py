import sys  #to interact with python runtine environemnt to get details about the errors
from src.logger import logging  #using logging function from logger file


def error_message_detail(error, error_detail:sys):  #error detail parameter is used as sys object
    _,_,exc_tb=error_detail.exc_info() #.exc_info function in sys module gives output as a tuple of type, value and traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # to retrieve the filename where the error occured from the traceback object
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))  # writing the format of the error message
    
    return error_message
    


class CustomException(Exception):  #creating a CustomeException class and inherting properties from built in Exception class
    def __init__(self,error_message, error_detail:sys): #special method in python class used to initiliaze the object's attribute or perform any setup required for the object
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self): #special method in python class used to convert an object into a string
        return self.error_message
    




