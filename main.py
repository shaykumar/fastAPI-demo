"""
Fast API Demo file
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """root function call for hello world"""
    return {"message": "Hello World"}


@app.get("/getTuple")
async def get_tuple():
    """function to return tuple"""
    return {
        "source_ip": "1.1.1.1",
        "source_port": "5100",
        "destination_ip": "2.2.2.2",
        "detination_port": "443",
    }
