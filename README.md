# Проект по GRPC сервису
Реализован через GRPC, Proto и Docker. Используется тестовая модель логистической регрессии ```models/model.pkl```, полученная с помощью скрипта ```make_sample_model.py```
## Docker контейнер
### Сборка:
```docker build -t grpc-ml-service .```
### Запуск:
```docker run -p 50051:50051 grpc-ml-service```
### Ожидаемый вывод:


## Обращение к серверу
### Узнать статус через grpcurl:
```grpcurl -plaintext localhost:50051 PredictionService.Health```
### Получить тестовое предсказание через ```client/client.py```:
```python -m client.client```
### Ожидаемый вывод: