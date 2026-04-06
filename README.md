# Real-Time Market Data Pipeline & API

## 🎯 Overview
An end-to-end Data Engineering pipeline that scrapes real-time trending market tickers, serves them via a FastAPI layer, and persists the data into an Enterprise PostgreSQL Warehouse using a Star Schema.

## 🏗️ Architecture
1. **Scraper:** Selenium (Headless) with anti-bot bypass logic.
2. **API:** FastAPI provides a JSON endpoint for real-time consumption.
3. **Warehouse:** PostgreSQL database using Fact and Dimension tables (Star Schema).
4. **ETL:** Python script to extract from API, transform data, and load into Postgres.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Automation:** Selenium (Chrome Driver)
- **Framework:** FastAPI, Uvicorn
- **Database:** PostgreSQL
- **Libraries:** Pandas, SQLAlchemy, Psycopg2

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start the API: `python main.py`
3. View API Docs: `http://127.0.0.1:8000/docs`
4. Run ETL to Database: `python database_loader.py`