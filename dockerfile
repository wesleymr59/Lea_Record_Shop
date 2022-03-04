# ===================================================================================================================
# - Dockerfile configurations
# ===================================================================================================================
ARG IMAGE_NAME="python" \
    IMAGE_VERSION="3.10.1-alpine3.15"
FROM ${IMAGE_NAME}:${IMAGE_VERSION}
LABEL DESCRIPTION="Lea_Record_Shop" 
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /usr/src/app
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]

# PS.: Create and save Python dependencies with the command:
# pip freeze > requirements.txt
#
# ===================================================================================================================
# - Docker - Creating Image and Container
# ===================================================================================================================
# Docker Build:
#
# docker image build -t Lea_Record_Shop:latest .
# -------------------------------------------------------------------------------------------------------------------
# Option 1 - Example of Docker Container RUN (in production):
#
# docker container run -it --name Lea_Record_Shop Lea_Record_Shop:latest
# -------------------------------------------------------------------------------------------------------------------
# Option 2 - Docker Container RUN (in development) sharing volume and creating renamed environment variables.
#
# docker container run -it -v $(pwd):/usr/src/app --env-file .env -p 81:80 --name Lea_Record_Shop Lea_Record_Shop:latest
# -------------------------------------------------------------------------------------------------------------------
#
# ===================================================================================================================
# - Start, Stop, Attach and Exec of created Container
# ===================================================================================================================
# Start Container by ID or Name:
#
# docker container start Lea_Record_Shop
# -------------------------------------------------------------------------------------------------------------------
# Stop Container by ID or Name:
#
# docker container stop Lea_Record_Shop
# -------------------------------------------------------------------------------------------------------------------
# Exec command in Container by ID or Name:
#
# docker container exec Lea_Record_Shop python --version
# docker container exec Lea_Record_Shop python seeder.py
# -------------------------------------------------------------------------------------------------------------------
# Attach Container by ID or Name:
#
# docker container attach Lea_Record_Shop