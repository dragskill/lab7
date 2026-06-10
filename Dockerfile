# Модель: Власний код (Метод градієнтного спуску)
# Автор: Шарапов Валерій Валерійович, група АІ-235

FROM python:3.10-slim
WORKDIR /app

RUN pip install fastapi uvicorn pydantic

COPY main.py .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-5000}"]