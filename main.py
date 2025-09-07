from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Hello World</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }
            h1 {
                text-align: center;
                margin-bottom: 30px;
                font-size: 2.5em;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .endpoint {
                background: rgba(255, 255, 255, 0.2);
                padding: 15px;
                margin: 15px 0;
                border-radius: 10px;
                border-left: 4px solid #4CAF50;
            }
            .method {
                font-weight: bold;
                color: #4CAF50;
                font-size: 1.1em;
            }
            .url {
                font-family: 'Courier New', monospace;
                background: rgba(0,0,0,0.2);
                padding: 5px 10px;
                border-radius: 5px;
                margin: 5px 0;
            }
            .description {
                margin-top: 10px;
                opacity: 0.9;
            }
            .docs-link {
                text-align: center;
                margin-top: 30px;
            }
            .docs-link a {
                color: #FFD700;
                text-decoration: none;
                font-size: 1.2em;
                padding: 10px 20px;
                background: rgba(255, 215, 0, 0.2);
                border-radius: 25px;
                transition: all 0.3s ease;
            }
            .docs-link a:hover {
                background: rgba(255, 215, 0, 0.4);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 FastAPI Hello World</h1>
            <p style="text-align: center; font-size: 1.2em; margin-bottom: 30px;">
                Добро пожаловать в простое FastAPI приложение!
            </p>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/helloworld</div>
                <div class="description">Возвращает приветственное сообщение "Hello, World!"</div>
            </div>
            
            <div class="endpoint">
                <div class="method">POST</div>
                <div class="url">/sum</div>
                <div class="description">Суммирует два числа. Принимает JSON: {"a": число1, "b": число2}</div>
            </div>
            
            <div class="docs-link">
                <a href="/docs" target="_blank">📚 Открыть документацию API</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

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
