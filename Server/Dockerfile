FROM python:2.7-slim
WORKDIR /
COPY . /
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
CMD ["python", "RunServer.py"]
