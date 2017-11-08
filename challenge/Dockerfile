FROM python:2.7

ENV PYTHONUNBUFFERED=1

EXPOSE 9999
WORKDIR /usr/src/app

# Copy the application 
COPY . /usr/src/app

RUN pip install -r requirements.txt
EXPOSE 9999

CMD ["python", "app.py"]
