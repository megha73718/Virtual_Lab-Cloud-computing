# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy current directory contents
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
