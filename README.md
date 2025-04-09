# Task 1: Развернуть  приложение  в контейнере

## Objective

Созданы Dockerfile, app.py, requirements.txt
## Steps

1. **Решение**
   - Созданы 3 файла. 
     - docker build -t lesta_task1 .
     - docker run -d --name=lesta_task1 -p 5000:5000 lesta_task1

2. **Проверка**
     - curl http://localhost:5000/ping

