from fastapi import FastApi

application = FastApi()

@application.get("/")
def root():
    return {"message": "init"}