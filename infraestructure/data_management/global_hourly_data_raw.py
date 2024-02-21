
from pandera.typing import Series
import pandera as pa


'''
Pandera: 
is a statistical typing and data testing tool 
for validating the properties of a dataframe's contents at runtime.
'''


'''
One Schema: for the raw data coming in from NOAA API called GlobalHourlyDataRaw
'''
class GlobalHourlyDataRaw(pa.SchemaModel):
    DATE: Series[pa.typing.DateTime]
    TMP: Series[str] #raw temperatur filed
    
    class Config: 
        coerce = True