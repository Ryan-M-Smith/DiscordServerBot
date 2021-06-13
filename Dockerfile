# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.6-slim-buster
#FROM python:3.7-slim-buster
#FROM python:3.8-slim-buster
#FROM python:3.9-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /src/
COPY . /src/

RUN pwd

# Creates a non-root user with an explicit UID and adds permission to access the /src folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" botuser && chown -R botuser /src
USER botuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "src/bot.py"]
