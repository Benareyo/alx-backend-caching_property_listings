# Use Python 3.12
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /code

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

