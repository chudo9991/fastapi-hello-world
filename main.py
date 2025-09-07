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
            .microphone-section {
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
                border-left: 4px solid #FF6B6B;
            }
            .microphone-status {
                display: flex;
                align-items: center;
                gap: 10px;
                margin: 10px 0;
            }
            .status-indicator {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #ccc;
            }
            .status-indicator.available {
                background: #4CAF50;
                box-shadow: 0 0 10px #4CAF50;
            }
            .status-indicator.denied {
                background: #f44336;
                box-shadow: 0 0 10px #f44336;
            }
            .status-indicator.checking {
                background: #ff9800;
                animation: pulse 1s infinite;
            }
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.5; }
                100% { opacity: 1; }
            }
            .mic-button {
                background: linear-gradient(45deg, #FF6B6B, #FF8E8E);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 1em;
                transition: all 0.3s ease;
                margin: 10px 5px;
            }
            .mic-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
            }
            .mic-button:disabled {
                background: #ccc;
                cursor: not-allowed;
                transform: none;
                box-shadow: none;
            }
            .mic-info {
                font-size: 0.9em;
                opacity: 0.8;
                margin-top: 10px;
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
            
            <div class="microphone-section">
                <h3>🎤 Проверка микрофона</h3>
                <div class="microphone-status">
                    <div class="status-indicator" id="micStatus"></div>
                    <span id="micStatusText">Статус микрофона неизвестен</span>
                </div>
                <button class="mic-button" id="checkMicBtn" onclick="checkMicrophone()">
                    Проверить микрофон
                </button>
                <button class="mic-button" id="requestMicBtn" onclick="requestMicrophonePermission()" style="display: none;">
                    Запросить разрешение
                </button>
                <div class="mic-info" id="micInfo">
                    Нажмите "Проверить микрофон" для проверки доступности и разрешений
                </div>
            </div>
            
            <div class="docs-link">
                <a href="/docs" target="_blank">📚 Открыть документацию API</a>
            </div>
        </div>
        
        <script>
            let mediaStream = null;
            
            // Функция для проверки доступности микрофона
            async function checkMicrophone() {
                const statusIndicator = document.getElementById('micStatus');
                const statusText = document.getElementById('micStatusText');
                const checkBtn = document.getElementById('checkMicBtn');
                const requestBtn = document.getElementById('requestMicBtn');
                const micInfo = document.getElementById('micInfo');
                
                // Показываем состояние "проверка"
                statusIndicator.className = 'status-indicator checking';
                statusText.textContent = 'Проверка доступности микрофона...';
                checkBtn.disabled = true;
                micInfo.textContent = 'Проверяем доступность микрофона...';
                
                try {
                    // Проверяем поддержку getUserMedia
                    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                        throw new Error('getUserMedia не поддерживается в этом браузере');
                    }
                    
                    // Проверяем разрешения
                    const permissionStatus = await navigator.permissions.query({ name: 'microphone' });
                    
                    if (permissionStatus.state === 'granted') {
                        // Разрешение уже дано, проверяем доступность
                        await testMicrophoneAccess();
                        updateStatus('available', 'Микрофон доступен и разрешен', 'Микрофон готов к использованию');
                        requestBtn.style.display = 'none';
                    } else if (permissionStatus.state === 'denied') {
                        // Разрешение отклонено
                        updateStatus('denied', 'Доступ к микрофону запрещен', 'Разрешение на использование микрофона было отклонено. Проверьте настройки браузера.');
                        requestBtn.style.display = 'none';
                    } else {
                        // Разрешение не запрашивалось
                        updateStatus('denied', 'Требуется разрешение на микрофон', 'Нажмите "Запросить разрешение" для доступа к микрофону');
                        requestBtn.style.display = 'inline-block';
                    }
                    
                } catch (error) {
                    console.error('Ошибка при проверке микрофона:', error);
                    updateStatus('denied', 'Ошибка доступа к микрофону', `Ошибка: ${error.message}`);
                    requestBtn.style.display = 'none';
                } finally {
                    checkBtn.disabled = false;
                }
            }
            
            // Функция для тестирования доступа к микрофону
            async function testMicrophoneAccess() {
                return new Promise((resolve, reject) => {
                    navigator.mediaDevices.getUserMedia({ audio: true })
                        .then(stream => {
                            // Если получили поток, сразу его останавливаем
                            stream.getTracks().forEach(track => track.stop());
                            resolve();
                        })
                        .catch(reject);
                });
            }
            
            // Функция для запроса разрешения на микрофон
            async function requestMicrophonePermission() {
                const statusIndicator = document.getElementById('micStatus');
                const statusText = document.getElementById('micStatusText');
                const requestBtn = document.getElementById('requestMicBtn');
                const micInfo = document.getElementById('micInfo');
                
                statusIndicator.className = 'status-indicator checking';
                statusText.textContent = 'Запрос разрешения...';
                requestBtn.disabled = true;
                micInfo.textContent = 'Запрашиваем разрешение на использование микрофона...';
                
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    
                    // Если получили поток, значит разрешение дано
                    updateStatus('available', 'Разрешение получено!', 'Микрофон готов к использованию');
                    requestBtn.style.display = 'none';
                    
                    // Останавливаем поток, так как мы только проверяли разрешение
                    stream.getTracks().forEach(track => track.stop());
                    
                } catch (error) {
                    console.error('Ошибка при запросе разрешения:', error);
                    
                    if (error.name === 'NotAllowedError') {
                        updateStatus('denied', 'Разрешение отклонено', 'Пользователь отклонил запрос на доступ к микрофону');
                    } else if (error.name === 'NotFoundError') {
                        updateStatus('denied', 'Микрофон не найден', 'На устройстве не обнаружен микрофон');
                    } else if (error.name === 'NotReadableError') {
                        updateStatus('denied', 'Микрофон недоступен', 'Микрофон используется другим приложением');
                    } else {
                        updateStatus('denied', 'Ошибка доступа', `Ошибка: ${error.message}`);
                    }
                    requestBtn.style.display = 'none';
                } finally {
                    requestBtn.disabled = false;
                }
            }
            
            // Функция для обновления статуса
            function updateStatus(status, text, info) {
                const statusIndicator = document.getElementById('micStatus');
                const statusText = document.getElementById('micStatusText');
                const micInfo = document.getElementById('micInfo');
                
                statusIndicator.className = `status-indicator ${status}`;
                statusText.textContent = text;
                micInfo.textContent = info;
            }
            
            // Автоматическая проверка при загрузке страницы
            window.addEventListener('load', () => {
                // Небольшая задержка для лучшего UX
                setTimeout(() => {
                    checkMicrophone();
                }, 1000);
            });
        </script>
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
