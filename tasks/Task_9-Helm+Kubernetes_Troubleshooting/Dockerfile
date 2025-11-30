
# Use lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose app port
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]


