FROM python:3.12

WORKDIR /app

# Instalar dependencias de Python
RUN apt update && apt upgrade -y \
    && apt install -y python3-pip python3-dev libpq-dev build-essential \
    && apt clean 


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]