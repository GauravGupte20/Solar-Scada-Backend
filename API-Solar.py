from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS for all origins (for Netlify to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/live")
def live_power(site: str = "demo"):
    # Return simulated live power in kW
    return {"kW": round(random.uniform(30, 150), 2)}

@app.get("/kpi")
def get_kpi(site: str = "demo"):
    # Return simulated daily KPIs
    return {
        "energy_today": round(random.uniform(400, 1200), 2),
        "energy_total": round(random.uniform(500000, 800000), 2),
        "pr": round(random.uniform(85, 95), 2)
    }
