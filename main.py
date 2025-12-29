from fastapi import FastAPI

# Create FastAPI application instance
app = FastAPI(
    title="Satellite Tracker API",
    description="An API for tracking satellites and calculating orbital parameters",
    version="1.0.0"
)

# Our first endpoint - a simple health check
@app.get("/")
def read_root():
    """
    Root endpoint - confirm the API is running
    """
    return {
        "message": "Satellite Tracker API is operational",
        "status": "nominal",
        "version": "1.0.0"
    }

# Information about the API
@app.get("/info")
def api_info():
    """
    Returns information about the API capabilities
    """
    return {
        "name": "Satellite Tracker API",
        "capabilities" : [
            "Satellite data management",
            "Orbital calculations",
            "Real-time tracking"
            ],
        "contact": "mission-control@techcoaches.info"
    }
        
