FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./
RUN pip3 install flask flask_restful
 

COPY . .

CMD [ "python3", "./main.py" ]