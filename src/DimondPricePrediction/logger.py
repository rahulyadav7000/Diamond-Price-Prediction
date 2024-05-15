import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Log_path = os.path.join(os.getcwd(),"logs")

os.makedirs(Log_path,exist_ok=True)

LOG_FILEPATH = os.path.join(Log_path,LOG_FILE)

logging.basicConfig(filename=LOG_FILEPATH,
                    level=logging.INFO,
                    format="[%(asctime)s] %(lineno)s - %(levelname)s - %(message)s")

