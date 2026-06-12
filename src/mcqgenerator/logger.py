import logging
import os
from datetime import datetime


Log_File=f"{datetime.now().strftime('%m_%m_%y_%H_%M_%S')}.log"

log_path =os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)

Log_Filepath = os.path.join(log_path,Log_File)

logging.basicConfig(
    level = logging.INFO,
    filename = Log_Filepath,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)