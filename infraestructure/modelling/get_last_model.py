
import datetime
from flytekit import dynamic

from models.model_update import ModelUpdate 


@dynamic(cache=True)
def get_latest_model(target_datetime: datetime,
                     genesis_datetime: datetime,
                     n_days_pretraining: int) -> ModelUpdate:
    print("get lastest model")
    