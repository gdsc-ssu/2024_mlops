from fastapi import FastAPI
from routers.a import a
import uvicorn

app = FastAPI()

app.include_router(a)

@app.get('/')
def home():
    return {'msg' : 'main'}

if __name__ == "__main__":
    uvicorn.run("main_2:app", host = '0.0.0.0', port=8000, reload = True)
