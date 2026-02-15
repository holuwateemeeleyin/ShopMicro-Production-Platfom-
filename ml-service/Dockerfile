# Use a slim version to save space
FROM python:3.12-slim
# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# Install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Security: Create and use a non-privileged user
RUN adduser --disabled-password appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]