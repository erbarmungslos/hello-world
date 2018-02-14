FROM python:3.6
COPY . /usr/src/app/flaskr
WORKDIR /usr/src/app/flaskr
RUN pip install --editable .
RUN pip install -r requirements.txt
ENV FLASK_APP=flaskr
ENV FLAS_DEBUG=true
CMD ["flask", "run"]
