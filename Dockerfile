# Simple Dockerfile for the demo Flask app
# Note: This intentionally includes a vulnerable dependency via requirements.txt for SCA demonstration

FROM python:3.11-slim

# Prevents Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency list and install first (leverages Docker layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py ./

# Expose Flask default port
EXPOSE 5000

# Run the app directly with Python (Flask app calls app.run)
CMD ["python", "app.py"]
