FROM python:3.8-alpine
RUN pip install flask
RUN mkdir /app
COPY ./static /app
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD ["app.py" ]