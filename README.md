# commodity-tracker
A Python microservice and dashboard that simulates real-time commodity market prices using FastAPI and visualizes live price trends with Streamlit, Pandas, and Plotly.
# 📈 Real-Time Commodity Price Tracker

A simple real-time commodity price tracker that uses a Python **FastAPI** backend to simulate live market prices and a **Streamlit** dashboard to visualize changing price trends using **Pandas** and **Plotly**.

## 🚀 Features

- ⚡ **FastAPI REST API** microservice serving mock commodity prices (Oil, Gold, Natural Gas, Silver)
- 🔄 Simulates realistic price fluctuations with each API call
- 📊 **Streamlit dashboard** displays live prices in a table and interactive line chart
- 🗂️ Persists price changes between calls to show meaningful time series trends
- ✅ Designed for practicing **microservices**, **APIs**, **data pipelines**, and **real-time visualization**

## 🗂️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** Streamlit, Pandas, Plotly Express
- **Other:** Requests (for API calls)

## 📦 Installation

Clone the repository and create a virtual environment:

git clone https://github.com/yourusername/commodity-price-tracker.git
cd commodity-price-tracker
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install fastapi uvicorn streamlit pandas plotly requests

## ⚙️ Running the Backend (FastAPI)

Start the FastAPI server:

uvicorn main:app --reload

Visit http://127.0.0.1:8000/prices to see live prices.

Use http://127.0.0.1:8000/docs for the auto-generated Swagger API docs.

## 🎛️ Running the Frontend (Streamlit)

Open a new terminal in the same virtual environment and run:

streamlit run dashboard.py

Visit http://localhost:8501 to view your live dashboard!

## ✅ Example API Response

{
  "prices": [
    {"name": "Oil", "price": 86.02},
    {"name": "Natural Gas", "price": 3.19},
    {"name": "Gold", "price": 1941.55},
    {"name": "Silver", "price": 24.65}
  ]
}

## 📸 Example Screenshot

(Add a screenshot once you run it!)

## 🔑 How It Works

- **FastAPI**: Acts as a backend microservice. Each request updates commodity prices with a small random change.
- **Streamlit**: Calls the API every few seconds, stores the price history, and plots a real-time line chart showing how prices change over time.

## 📂 Project Structure

commodity-price-tracker/
├── main.py           # FastAPI backend
├── dashboard.py      # Streamlit frontend
├── requirements.txt  # (Optional) dependencies list
├── README.txt        # Project documentation

## 🎯 Why This Project

This project demonstrates:
- Designing and building a **Python microservice**
- Working with **REST APIs**
- Simulating real-world data flows
- Building interactive **real-time dashboards**
- Skills relevant to **front office analytics**, trading tools, or data engineering


Open source for learning and portfolio use!

## 📬 Contact

[Isaac Mopa](https://www.linkedin.com/in/isaac-mopa) — always open to connect!


🚀 Happy coding!
