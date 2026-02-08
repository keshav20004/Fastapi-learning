from fastapi import FastAPI
app=FastAPI()


@app.get("/")
def hell0():
    return {"message" :"Hello from fastapi testing git too"}

@app.get("/about")
def about():
    return {"message":  "This is the info about keshav....he is an aiml student "}

