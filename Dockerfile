# Step 1: Use the official Python image as the base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Install system dependencies required for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

# Step 5: Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the rest of the project files to the container
COPY . /app/

# Step 8: Expose the necessary port (optional)
EXPOSE 8080

# Step 9: Run migrations and start the Django app using Gunicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn portfolio_backend.wsgi:application --bind 0.0.0.0:$PORT"]
