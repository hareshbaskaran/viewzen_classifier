# Use the official Python base image
FROM python:3.9-slim


# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080
EXPOSE 8051
# Run the FastAPI application using uvicorn server
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
#CMD ["uvicorn", "app.main:app"]
#CMD ["streamlt", "run", "app/app.py"]