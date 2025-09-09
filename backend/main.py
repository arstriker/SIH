import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

# --- 1. Pydantic Models for Structured Data ---
# These models ensure that the data exchanged between the frontend and backend is well-defined and validated.

class DiagnosisRemedy(BaseModel):
    """A single remedy for a plant disease."""
    type: str = Field(..., example="Organic")
    description: str = Field(..., example="Spray a solution of neem oil and water every 7 days.")

class DiagnosisResult(BaseModel):
    """The structured response for a visual diagnosis request."""
    disease_name: str = Field(..., example="Early Blight")
    confidence_score: float = Field(..., example=0.95)
    description: str = Field(..., example="A common fungal disease affecting tomatoes, characterized by yellow halos and concentric rings on leaves.")
    remedies: List[DiagnosisRemedy]

class DiaryEntry(BaseModel):
    """The structured data extracted from a user's voice log."""
    action: Optional[str] = Field(None, example="bought")
    item: Optional[str] = Field(None, example="potash")
    quantity: Optional[str] = Field(None, example="10 kg")
    cost: Optional[str] = Field(None, example="500 rupees")

class DiaryLogConfirmation(BaseModel):
    """Confirmation response after logging a diary entry."""
    status: str = "success"
    logged_entry: DiaryEntry

class Advice(BaseModel):
    """A single piece of actionable advice."""
    task: str = Field(..., example="Check for pests, especially aphids, on the underside of new leaves.")

class AdviceResponse(BaseModel):
    """The structured response for a request for personalized advice."""
    advice_list: List[Advice]


# --- 2. FastAPI Application Initialization ---
app = FastAPI(
    title="Krishi Aashaan API",
    description="Backend server for the AI-Powered Personal Farming Assistant.",
    version="1.0.0"
)


# --- 3. API Endpoints ---

@app.get("/")
def read_root():
    """A simple root endpoint to confirm the server is running."""
    return {"message": "Welcome to the Krishi Aashaan Backend!"}

@app.post("/diagnose", response_model=DiagnosisResult)
async def diagnose_plant(image: UploadFile = File(...)):
    """
    Endpoint for visual pest/disease diagnosis.
    In a real application, this endpoint would send the image to the Gemini API.
    Here, we simulate the API's response.
    """
    # --- GEMINI API PROMPT (FOR SIMULATION) ---
    # The prompt sent to the Gemini API would be:
    # "You are an expert agronomist specializing in crops grown in Kerala, India.
    # Analyze the following image of a plant leaf. Identify the specific disease or
    # pest affecting it. Provide a confidence score for your diagnosis. Then, list practical,
    # step-by-step remedies, including both organic and chemical options suitable for a
    # smallholder farmer. Return the result as a structured JSON object."

    # Simulate receiving the image data
    image_data = await image.read()
    print(f"Received image '{image.filename}' of size {len(image_data)} bytes.")

    # Simulate a successful API response from Gemini
    return DiagnosisResult(
        disease_name="Early Blight (Simulated)",
        confidence_score=0.92,
        description="A common fungal disease affecting tomatoes and potatoes. It appears as small, brown lesions, primarily on lower, older leaves.",
        remedies=[
            DiagnosisRemedy(type="Organic", description="Remove and destroy affected lower leaves. Spray with a neem oil solution (2ml per liter of water) every 7-10 days."),
            DiagnosisRemedy(type="Chemical", description="Apply a copper-based fungicide (e.g., Mancozeb) according to package directions, ensuring full coverage of the plant.")
        ]
    )

@app.post("/log_diary", response_model=DiaryLogConfirmation)
async def log_diary_entry(text: str = Form(...)):
    """
    Endpoint for logging a farm diary entry from transcribed Malayalam text.
    In a real application, this sends the text to Gemini for data extraction.
    Here, we simulate the API's response.
    """
    # --- GEMINI API PROMPT (FOR SIMULATION) ---
    # The prompt sent to the Gemini API would be:
    # "You are a data extraction assistant. Analyze the following Malayalam text and
    # extract the key farming activity details. Identify the 'action' (e.g., bought,
    # applied, harvested), the 'item' (e.g., potash, urea), the 'quantity'
    # (e.g., 10 kg), and the 'cost' (e.g., 500 rupees). Return these details in a
    # structured JSON format. If a piece of information is missing, set its value to null."

    print(f"Received text for diary log: '{text}'")

    # Simulate a successful API response from Gemini based on example
    # Example: "ഇന്ന് 500 രൂപക്ക് 10 കിലോ പൊട്ടാഷ് വാങ്ങി"
    return DiaryLogConfirmation(
        logged_entry=DiaryEntry(
            action="bought",
            item="potash",
            quantity="10 kg",
            cost="500 rupees"
        )
    )

@app.get("/get_advice", response_model=AdviceResponse)
async def get_farmer_advice():
    """
    Endpoint for getting personalized, actionable advice.
    In a real application, this would send farmer context to Gemini.
    Here, we simulate the API's response.
    """
    # --- GEMINI API PROMPT (FOR SIMULATION) ---
    # The prompt sent to the Gemini API would be:
    # "Acting as a personal farming advisor for a farmer in Kerala, given the following
    # context: [Crop: Tomato, Age: 45 days, Recent Log: Bought fungicide, Weather:
    # Light rain expected in 2 days], provide a short, simple, and actionable list of
    # 2-3 tasks the farmer should prioritize today or this week. The advice should be in
    # simple language. Return a structured JSON object."

    print("Fetching personalized advice.")

    # Simulate a successful API response from Gemini
    return AdviceResponse(
        advice_list=[
            Advice(task="Monitor soil moisture. Avoid overwatering as rain is expected."),
            Advice(task="Since you recently bought fungicide, consider a preventative spray before the rain if conditions are humid."),
            Advice(task="Look for and remove any new leaves showing signs of blight.")
        ]
    )

# --- 4. Running the Application ---
# This allows running the server directly for development.
# Command: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
