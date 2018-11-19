FROM python:2.7
COPY . /
WORKDIR /
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV CONF docker
CMD ["python", "-u", "RunServer.py"]