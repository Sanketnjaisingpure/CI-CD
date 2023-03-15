import sys 
import logger
import logging
# provides functions and variables that are used to manipulate different parts of that python runtime env

def error_message_details(error , error_detail:sys):
    """ if any message happen we can give that our custom messages
    """
    _,_,exc_tb =error_detail.exc_info()
    
    # This will gives you three information , the last info (exc_tb) it will gives you all the infomation about in 
    # file the exception has occur and in which line the exceptions has occur

    
    file_name = exc_tb.tb_frame.f_code.co_filename # above code gives use the file name where error occured

    line_number = exc_tb.tb_lineno



    error_message = "Error Occured in python Script name [{0}] line number [{1}] error message[{2}]".format(

        file_name , line_number , str(error)
    )

    return error_message

class CustomException(Exception):

    def __init__(self , error_message , error_details:sys):

        super().__init__(error_message)

        self.error_message = error_message_details(error_message , error_detail=error_details)

       

    def __str__(self) -> str:

        return self.error_message


        