from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gradio_client import Client

# =========================
# APP
# =========================
app = FastAPI(title="Industry Prediction API")

# =========================
# GRADIO CLIENT
# =========================
client = Client("Traii/predict-industry-api")

# =========================
# REQUEST MODEL
# =========================
class ServiceRequest(BaseModel):
    service: str

# =========================
# API ENDPOINT
# =========================
@app.post("/predict-service")
def predict_service(data: ServiceRequest):

    try:
        result = client.predict(
            service=data.service,
            api_name="/predict_service"
        )

        return {
            "success": True,
            "input": data.service,
            "prediction": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
