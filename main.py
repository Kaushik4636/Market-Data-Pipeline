from fastapi import FastAPI
from scraper import scrape_trending_tickers
import uvicorn

# 1. Initialize the API
app = FastAPI(title="Real-Time Market Data API")

@app.get("/")
def home():
    return {"message": "Market Data API is Online. Go to /trending to see data."}

@app.get("/trending")
def get_trending():
    print("🚀 API Request received! Triggering Scraper...")
    data = scrape_trending_tickers()
    
    if not data:
        return {"status": "error", "message": "Failed to fetch data from Yahoo Finance"}
    
    return {"status": "success", "count": len(data), "data": data}

if __name__ == "__main__":
    # Run the server
    uvicorn.run(app, host="127.0.0.1", port=8000)