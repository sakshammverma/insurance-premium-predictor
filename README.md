# Insurance Premium Predictor (End-to-End ML Project)

Hi! Welcome to my **Insurance Premium Prediction** project. 

This is a full-stack Machine Learning application I built to solve a real-world problem: **estimating health insurance costs based on personal health data.**

Instead of just building a model in a notebook, I turned it into a fully functional web application. I trained a Machine Learning model, wrapped it in a **FastAPI** backend, and built a user-friendly **Streamlit** dashboard so anyone can use it interactively.

##  What This Project Does
* **Predicts Costs:** Uses a trained ML model (Random Forest/Linear Regression) to estimate insurance premiums.
* **Interactive UI:** A clean **Streamlit** frontend where users can enter details like Age, BMI, and Smoking status to get an instant prediction.
* **REST API:** A robust **FastAPI** backend that serves the model, handles data validation, and manages requests.
* **Data Validation:** Uses **Pydantic** schemas to ensure that inputs (like negative age or invalid region) are caught before they reach the model.

##  Tech Stack
* **Language:** Python 3.12
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Backend Framework:** FastAPI, Uvicorn
* **Frontend Framework:** Streamlit
* **Data Validation:** Pydantic

##  Project Structure
```bash
├── app.py                  # Main FastAPI application
├── requirements.txt        # Project dependencies
├── insurance.csv           # Dataset used for training
├── frontend/
│   └── frontend.py         # Streamlit User Interface
├── model/
│   ├── model_train.py      # Script to train and save the model
│   ├── predict.py          # Logic for loading model & making predictions
│   └── model.pkl           # The saved trained model
└── schema/
    └── user_input.py       # Pydantic models for data validation
```
 ## How to Run It Locally
 
### 1. Clone the Repository
Open your terminal and run:
  ```bash
  git clone https://github.com/sakshammverma/insurance-premium-predictor.git
```
### 2.Run the backend
```bash
  uvicorn app:app --reload
```
### 3. Start frontend
```bash
streamlit run frontend/frontend.py
```


Built by Saksham Verma with guidance of CampusX




