import logging #to write logging messages
import os #to navigate the file system and create a directory for logs
from datetime import datetime #to use date and time for log messages


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # creating a log file filename for current time with the specified date format
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  #creating a directory path where log files will be stored
os.makedirs(logs_path,exist_ok=True)  #creating a separate directory for log files if it doesn't already exists.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)  #creating the full path to the log file by joining logs path directory and log file filename.

#configuring loging system with basic configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,  #specifying filename for the log file
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  #specifying the format of the log message as timestamp, line number, logger name, log level, log message 
    level=logging.INFO,  #This line sets the logging level to INFO, indicating that only log messages with a level of INFO or higher will be logged. 

)
    
