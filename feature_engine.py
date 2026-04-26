def build_task(feature, config):
    
    if feature == "ml_predict":
        return {
            "task_type": "predict",
            "payload": config
        }

    elif feature == "health_check":
        return {
            "task_type": "health",
            "payload": {}
        }

    return {"error": "Unknown feature"}
