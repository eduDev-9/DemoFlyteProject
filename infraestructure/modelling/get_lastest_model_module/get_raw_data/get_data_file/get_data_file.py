#Flyte
import pandera as pa
from pandera.typing import DataFrame
#External Library
import pandas as pd
#Python
import requests
import time
from io import StringIO
#Common
from common.constants.constants import DATA_ACCESS_URL
 # Data Managment Layer
from infraestructure.data_management.global_hourly_data_raw import GlobalHourlyDataRaw

class GetDataFile:
    
    @pa.check_types
    def get_data_file(filepath: str) -> DataFrame[GlobalHourlyDataRaw]:
        """Get raw data file from global hourly remote archive.

        https://www.ncei.noaa.gov/data/global-hourly

        NOTE: the `start_date` and `end_date` arguments are primarily for caching. 
        The filepath points to a remote csv file that is frequently updated, 
        so this task needs to know from the API response whether the `end_date` has
        changed so this task can fetch an updated version of the csv.
        """
        
        if filepath.startswith("/"):
            filepath = filepath[1:] # get a substring (data/global-hourly)
            response = requests.get(f"{DATA_ACCESS_URL}/{filepath}") #GET
            time.sleep(0.25) #limit to four request per second
            return pd.read_csv(StringIO(response.text), low_memory=False)
        raise RuntimeError(
            f"could not get raw data file {filepath} from {DATA_ACCESS_URL}"
        )