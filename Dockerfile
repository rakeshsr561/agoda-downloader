FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT /bin/bash
CMD ["python", "application.py"]
