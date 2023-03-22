import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #File Name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   # join current path of folder with file name
os.makedirs(logs_path,exist_ok=True)   #Make directory (folder) of at that path

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) 


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)
