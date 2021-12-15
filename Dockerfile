FROM python:3.8-alpine

## Setup Shoppy
COPY . /usr/src/preis/
WORKDIR /usr/src/preis
ENV DEBUG='False'
RUN pip3 install -r requirements.txt && rm requirements.txt
RUN chmod u+x ./entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
