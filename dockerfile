FROM python:3.13

RUN mkdir app/

WORKDIR /app

COPY ./ ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]