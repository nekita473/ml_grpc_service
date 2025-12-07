# Проект по GRPC сервису
Реализован через GRPC, Proto и Docker. Используется тестовая модель логистической регрессии ```models/model.pkl```, полученная с помощью скрипта ```make_sample_model.py```
## Docker контейнер
### Сборка:
```docker build -t grpc-ml-service .```
### Запуск:
```docker run -p 50051:50051 grpc-ml-service```
### Ожидаемый вывод:
<img width="1086" height="443" alt="Screenshot 2025-12-07 034257" src="https://github.com/user-attachments/assets/3604563f-86f5-4183-82cb-c1b509188278" />

## Обращение к серверу
### Узнать статус через grpcurl:
```grpcurl -plaintext localhost:50051 PredictionService.Health```
### Получить тестовое предсказание через ```client/client.py```:
```python -m client.client```
### Ожидаемый вывод:
<img width="926" height="136" alt="Screenshot 2025-12-07 034352" src="https://github.com/user-attachments/assets/388cf4d3-c8e9-4224-87a6-8cab8d532576" />
