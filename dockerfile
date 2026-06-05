from python:3.10-slim

workdir /app
copy requirements.txt .
run pip install -r requirements.txt
copy app.py .
expose 3000
cmd ["python","app.py"]