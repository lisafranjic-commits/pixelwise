from fastapi import FastAPI, Request, Depends
from app.auth import verify_api_key
from pydantic import BaseModel
import numpy as np
from app.classifier import classify_batch
from app.models import Prediction, SessionLocal

class ClassifyRequest(BaseModel):
    pixels: list[list[int]]


class ClassifyResponse(BaseModel):
    prediction: str
    confidence: float
    scores: dict[str, float]


app = FastAPI()


@app.get("/api/health")
def health():
    return {"status": "ok", "model_version": "v1"}


@app.get("/api/results")
def results():
    db = SessionLocal()
    rows = (
        db.query(Prediction)
        .order_by(Prediction.created_at.desc())
        .limit(20)
        .all()
    )
    db.close()

    return {
        "results": [
            {
                "id": r.id,
                "prediction": r.prediction,
                "confidence": r.confidence,
                "model_version": r.model_version,
                "created_at": r.created_at.isoformat()
            }
            for r in rows
        ]
    }




@app.post( "/api/classify",
    response_model=ClassifyResponse,
    dependencies=[Depends(verify_api_key)])

def classify(request: Request, req: ClassifyRequest):
    arr = np.array(req.pixels, dtype=np.uint8)[np.newaxis]
    result = classify_batch(arr)[0]

    db = SessionLocal()
    db.add(
        Prediction(
            prediction=result["prediction"],
            confidence=result["confidence"],
            model_version="v1"
        )
    )
    db.commit()
    db.close()

    return result

