from pandera.typing import Series, Index
import pandera as pa


'''
Pandera: 
is a statistical typing and data testing tool 
for validating the properties of a dataframe's contents at runtime.
'''


'''
Second Schema: for the expected type of the dataframe once we've cleaned it and is model-ready.
'''
class GlobalHourlyData(pa.SchemaModel):
    # validate the min and max temperature range in degrees Celsius
    air_temp: Series[float] = pa.Field(ge= -273.15, le=459.67)
    dew_temp: Series[float] = pa.Field(ge= -273.15, le=459.67)
    
    # pandera supports validating pandas.Index
    data: Index[pa.typing.DateTime] = pa.Field(unique=True)
    
    class Config: 
        coerce = True