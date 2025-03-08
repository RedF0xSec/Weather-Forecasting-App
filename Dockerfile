FROM python:3.10.9-slim-buster
LABEL authors="Utente"

WORKDIR /weather

# Copy requirements
COPY requirements.txt ./requirements.txt

# Install dependencies and clean up to reduce image size
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxrender1 \
    gcc \
    g++ \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip3 install --upgrade pip setuptools "setuptools>=70.0" && \
    pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Copy all the files needes for the application
ADD data /weather/data
COPY app_pipeline.py /weather
ADD models /weather/models
ADD imgs /weather/imgs
ADD logs /weather/logs

# Create an entry point to make the image executable
ENTRYPOINT ["streamlit", "run"]
CMD ["app_pipeline.py"]



