import sys # we are using sys library because it will tell us the filename , line no on the system where we are getting the error 
from src.logger import logging

class CustomException(Exception):
    
    def __init__(self,error,sys):
        super().__init__()
        self.sys=sys
        self.error=error
        _,_,exc_tb = self.sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in python script name {file_name} line number {exc_tb.tb_lineno} , error message {str(self.error)}"
        self.error_message=error_message
    
    def __str__(self): # we use __str__ (string method) here because we need a class method that doesn't require to be called __str__ returns string
        
        return self.error_message

     
    
# Example code 
# This is how we will do the logging and exception handline throughout projects as it is done below 
if __name__=="__main__":
    logging.info("Logging has started") # this will tell what actually is happening right now in the code , will get saved in the logs folder 

    try:
        a=1/0 # here we will write all our code that we are working with 
    except Exception as e:
        logging.info('Division by zero') 
        raise CustomException(e,sys) # this we will use everywhere after the code , in case if code didn't work then error will be recorded in the logs file