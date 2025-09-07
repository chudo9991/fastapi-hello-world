# FastAPI Hello World

Простое FastAPI приложение с двумя эндпоинтами: `/helloworld` и `/sum`.

## Эндпоинты

- `GET /` - Главная страница
- `GET /helloworld` - Возвращает "Hello, World!"
- `POST /sum` - Суммирует два числа

## Запуск с Docker Compose

1. Убедитесь, что у вас установлены Docker и Docker Compose
2. Запустите приложение:
   ```bash
   docker-compose up --build
   ```
3. Приложение будет доступно по адресу: http://localhost:8000
4. Документация API доступна по адресу: http://localhost:8000/docs

## Примеры использования

### Hello World
```bash
curl http://localhost:8000/helloworld
```

### Сумма двух чисел
```bash
curl -X POST "http://localhost:8000/sum" \
     -H "Content-Type: application/json" \
     -d '{"a": 5, "b": 3}'
```

## Остановка приложения

```bash
docker-compose down
```
