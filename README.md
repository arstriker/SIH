# Krishi Aashaan: AI-Powered Personal Farming Assistant

This repository contains the source code for "Krishi Aashaan," a mobile-first application that acts as a personal AI farming assistant for smallholder farmers in Kerala, India.

## Project Structure

The project is divided into two main components:

- **/backend**: A Python application using the FastAPI framework. It serves as the API backend, handling business logic and simulating interactions with the Google Gemini API.
- **/frontend**: A Flutter application that provides the mobile user interface. It is designed to be simple, intuitive, and mobile-first.

```
.
├── backend
│   ├── main.py         # FastAPI application with all API endpoints
│   └── requirements.txt  # Python dependencies
└── frontend
    └── krishi_aashaan_app
        ├── lib
        │   ├── main.dart # Main Flutter application entry point
        │   └── screens     # UI screens for each feature
        │       ├── aashaan_screen.dart
        │       ├── dashboard_screen.dart
        │       └── nottam_screen.dart
        └── pubspec.yaml    # Flutter dependencies
```

## Core Features

1.  **AI-Powered Visual Diagnosis ("Nottam")**: Farmers can upload a photo of a plant to get an AI-driven diagnosis of diseases or pests.
2.  **Voice-Powered Farm Diary ("Krishi Diary")**: Farmers can log their daily activities using natural voice commands in Malayalam.
3.  **Personalized Actionable Advice**: The application provides daily, context-aware tasks and recommendations.

## Getting Started

### 1. Running the Backend Server

The backend server is required for the frontend application to function correctly.

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
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    The server will be available at `http://localhost:8000`.

### 2. Running the Frontend Application

The frontend is a Flutter application.

1.  **Ensure you have the Flutter SDK installed.**

2.  **Navigate to the frontend directory:**
    ```bash
    cd frontend/krishi_aashaan_app
    ```

3.  **Install Flutter dependencies:**
    ```bash
    flutter pub get
    ```

4.  **Run the application:**
    Connect a device or start an emulator, and then run:
    ```bash
    flutter run
    ```
    The application will build and install on your device. Note that for the app to work, the backend server must be running and accessible from the device/emulator. You may need to change the API endpoint in the Flutter code to point to your computer's local IP address (e.g., `http://192.168.1.10:8000`) instead of `localhost`.
