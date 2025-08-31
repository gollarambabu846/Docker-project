FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py init_db.py ./

# Initialize the database when building the image
RUN python init_db.py

EXPOSE 5000

CMD ["python", "app.py"]
