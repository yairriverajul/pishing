# Use official slim Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose the port Render will route traffic to
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
