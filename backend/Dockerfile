# Use Python 3.12.11 as base image
FROM python:3.12.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional: curl, build tools, etc. if needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend app files
COPY . .

# Expose the Render-assigned port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
