FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

EXPOSE 8080/tcp
ENV FLASK_PORT=8080

WORKDIR /planety
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
