

from typing import List

from pandera.typing import DataFrame
import pandas as pd

from infraestructure.data_management.global_hourly_data_raw import GlobalHourlyDataRaw
from infraestructure.modelling.get_lastest_model_module.get_raw_data.get_data_file.get_data_file import GetDataFile

class GetRawData:
    
    def __init__(self, module:GetDataFile) -> None:
        self.module = module
        
    
    def get_raw_data(self, responses: List[dict]) -> DataFrame[GlobalHourlyDataRaw]:
        data = []
        #logger.debug(f"found {len(responses)} responses")
        
        # TODO: figure out how to not cache a data file if doesn't contain data for all hours of the day
        for response in responses:
            for station in response["stations"]:
                print(f"station:{station['name']}")
            data.append(self.module.get_data_file(filepath=response['filepath']))
            
        return pd.concat(data)