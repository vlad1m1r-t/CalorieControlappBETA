FROM python:3.10

# set work directory
WORKDIR /mysite

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]