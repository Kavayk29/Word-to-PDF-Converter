# Use an official Python runtime as a parent image
FROM python:3.10.15-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, including Pandoc
RUN apt-get update && \
    apt-get install -y pandoc

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    && rm -rf /var/lib/apt/lists/*


# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "app.py"]
