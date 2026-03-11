from fastapi import FastAPI

app = FastAPI()

targets=[]
currenID=1

@app.get("/")
def home():
    return targets

@app.post("/targets")
def add_target(target:dict):
    global currenID;

    target["id"]=currenID;
    targets.append(target);
    currenID+=1;

    return target

@app.get("/targets")
def get_targets():
    return targets

@app.delete("/target/{id}")
def delete_targets(id:int):
    global targets;
    targets=[t for t in targets if t["id"]!=id ]
    return {"message": "Silindi"}


    