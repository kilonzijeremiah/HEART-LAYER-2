from pydantic import BaseModel

class FeatureRequest(BaseModel):
    user_id: str
    feature: str
    config: dict
