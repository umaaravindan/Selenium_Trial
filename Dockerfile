From python:3.9-slim

WORKDIR C:\ProgramData\Jenkins\.jenkins\workspace\Selenium_JOB_working

ARG USERNAME
ARG PASSWORD
ARG REPOSITORY

# Set environment variables
ENV USERNAME=chatlearning123
ENV PASSWORD=1234567890
ENV REPOSITORY=https://hub.docker.com/repository/docker/chatlearning123/getting-started
ENV TAG=chatlearning123/getting-started:latest

COPY AmazonLogin.py .
COPY Input.csv .
COPY welcome.py .
 
RUN pip install pandas selenium

CMD ["python", "welcome.py"]
