from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a root route (homepage)
@app.get("/")
def read_root():
    return {"message": "Welcome to your first FastAPI app!"}