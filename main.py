from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title="FastAPI Hello World",
    description="Простое FastAPI приложение с двумя эндпоинтами",
    version="1.0.0"
)

class SumRequest(BaseModel):
    a: Union[int, float]
    b: Union[int, float]

class SumResponse(BaseModel):
    result: Union[int, float]

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в FastAPI Hello World!"}

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello, World!"}

@app.post("/sum", response_model=SumResponse)
async def sum_numbers(request: SumRequest):
    result = request.a + request.b
    return SumResponse(result=result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
