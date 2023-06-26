# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python file into the container
COPY globals.py .
COPY cv_upload_response_page.py .


# Expose the default Streamlit port
EXPOSE 8501

# Set the entry point for the container
CMD ["streamlit", "run", "cv_upload_response_page.py"]