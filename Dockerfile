FROM python:3.7
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install gunicorn
RUN pip install -r requirements.txt
ENV PORT=8000
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
