# - Dockerfile configurations

ARG IMAGE_NAME="python" \
    IMAGE_VERSION="3.10.1-alpine3.15"
FROM ${IMAGE_NAME}:${IMAGE_VERSION}
LABEL DESCRIPTION="Lea_Record_Shop" 
COPY requirements.txt /
RUN python3 -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt
WORKDIR /usr/src/app
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]
