from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# model
class BMIInput(BaseModel):
    height: float
    weight: float

# BMI classify
def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# POST endpoint
@app.post("/calculate_bmi")
def calculate_bmi(data: BMIInput):
    if data.height <= 0 or data.weight <= 0:
        raise HTTPException(status_code=400, detail="Height and weight must be positive values.")

    bmi = data.weight / (data.height ** 2)
    classification = classify_bmi(bmi)

    return {
        "bmi": round(bmi, 2),
        "classification": classification
    }
