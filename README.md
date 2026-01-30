# Patient Management System (FastAPI)

Hi! This is a backend project I built to learn **FastAPI**. It's a REST API that helps manage patient records. You can create new patients, update their details, and delete them (CRUD operations).

One cool feature I added is **automatic BMI calculation**—when you add a patient's height and weight, the system automatically calculates their BMI and gives a health verdict (like "Normal" or "Overweight") without you having to type it in.

## Features
* **Create Patients:** Add new records with validation (e.g., age must be positive).
* **Smart Logic:** Automatically calculates `BMI` and `Verdict` based on height and weight.
* **Read & Search:** View all patients or search for a specific one by ID.
* **Update Data:** You can update just one field (like changing a name) without rewriting the whole record.
* **Sorting:** You can sort the patient list by Age, Weight, or BMI.
* **Storage:** Uses a local `patients.json` file to save data, so it persists even if you restart the server.

## 🛠️ How I Built It
* **Language:** Python 3.12
* **Framework:** FastAPI
* **Validation:** Pydantic 
* **Server:** Uvicorn

## How to Run it on Your Machine

1. **Clone my repo**
   ```bash
   git clone https://github.com/sakshammverma/insurance-premium-predictor.git

2. **Install requiremenmts**
   ```bash
    pip install -r requirement.txt
    
3.  **Start the server***
    ```bash
     uvicorn app:app --reload
4. Start frontend
   ```bash
   streamlit run frontend.py
