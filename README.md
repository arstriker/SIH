# Krishi Aashaan: AI-Powered Personal Farming Assistant

This repository contains the source code for "Krishi Aashaan," a mobile-first web application that acts as a personal AI farming assistant for smallholder farmers in Kerala, India.

## Project Structure

The project is divided into two main components:

-   **/backend**: A Python application using the FastAPI framework. It serves as the API backend, handling business logic and simulating interactions with the Google Gemini API.
-   **/frontend**: A mobile-first web interface built with standard HTML, CSS, and JavaScript.

```
.
├── backend
│   ├── main.py         # FastAPI application with all API endpoints
│   └── requirements.txt  # Python dependencies
└── frontend
    └── web
        ├── index.html    # Main HTML file for the web interface
        ├── style.css     # CSS for styling
        └── script.js     # JavaScript for interactivity and API calls
```
*(Note: A directory for a previous Flutter-based implementation, `frontend/krishi_aashaan_app`, may still exist but is deprecated and not in use.)*

## Core Features

1.  **AI-Powered Visual Diagnosis ("Nottam")**: Farmers can upload a photo of a plant to get an AI-driven diagnosis of diseases or pests.
2.  **Text-Powered Farm Diary ("Aashaan")**: Farmers can log their daily activities using text input.
3.  **Personalized Actionable Advice**: The application provides daily, context-aware tasks and recommendations.

## Getting Started

To run this application, you need to run both the backend API and a local server for the frontend web interface.

### 1. Running the Backend Server

The backend API must be running for the frontend to function.

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the FastAPI server:**
    ```bash
    # This will run the backend on http://localhost:8000
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    Keep this terminal running.

### 2. Running the Frontend Web Interface

The frontend is a static web page, but it must be served by a local web server for the JavaScript to be able to make API calls to the backend (due to browser security policies).

1.  **Open a new terminal window.**

2.  **Navigate to the web frontend directory:**
    ```bash
    cd frontend/web
    ```

3.  **Start a simple Python web server on a different port (e.g., 8001):**
    ```bash
    # For Python 3
    python -m http.server 8001
    ```
    *If you have Python 2, the command is `python -m SimpleHTTPServer 8001`.*

4.  **Open your web browser** (preferably in its mobile view for the intended experience) and navigate to:
    `http://localhost:8001`

You should now see the Krishi Aashaan web interface. All features will make live calls to your running backend server.
