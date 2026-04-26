from fastapi import FastAPI
from schemas import FeatureRequest
from engines.feature_engine import build_task
import requests

app = FastAPI(title="Brain API")

HEART_URL = "https://heart-layer-production.up.railway.app"

@app.post("/build")
def build_feature(req: FeatureRequest):

    task = build_task(req.feature, req.config)

    # send to heart
    res = requests.post(
        f"{HEART_URL}/internal/execute",
        json={
            "project_id": req.user_id,
            "task_type": task["task_type"],
            "payload": task["payload"]
        }
    )

    return {
        "status": "sent_to_heart",
        "task": task
    }
