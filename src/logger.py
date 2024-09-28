# Logging is a means of tracking events that happen when some software runs.
import logging      #This module provides tools to report status, errors, and informational messages in applications.
import os       #The os module allows interaction with the operating system, including file path manipulation and directory creation.
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #Appends the .log extension to the formatted date and time, creating a unique log file name for each time the script runs, e.g., 09_28_2024_15_30_45.log.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Combines the current directory, a subdirectory called "logs," and the log file name into one path. This path points to where the log file will be stored, e.g., /current/directory/logs/09_28_2024_15_30_45.log
os.makedirs(logs_path,exist_ok=True)    #This creates the directory specified by logs_path. The exist_ok=True argument ensures that no error is raised if the directory already exists.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, #Sets the logging level to INFO, meaning only events with severity level INFO or higher will be logged.


)