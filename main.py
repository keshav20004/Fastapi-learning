from fastapi import FastAPI
app=FastAPI()


@app.get("/")
def hell0():
    return {"message" :"Hello from fastapi testing git too"}