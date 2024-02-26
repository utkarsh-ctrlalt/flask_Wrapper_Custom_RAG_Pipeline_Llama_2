# Use Python 3.11 slim image as base
FROM python:3.11-slim AS base

# Update package lists
RUN apt-get -y update

# Install necessary system packages
RUN apt-get install build-essential -y
RUN apt-get install git -y
RUN apt-get install wget -y

# Set environment variables for application
ENV APP_HOME /srv
ENV PORT 8502

# Set the working directory to /srv
WORKDIR $APP_HOME


# Clone the GitHub repository into the working directory
RUN git clone -b main https://github.com/utkarsh-ctrlalt/flask_Wrapper_Custom_RAG_Pipeline_Llama_2.git .

# Copy the requirements.txt file into the working directory
COPY requirements.txt $APP_HOME/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download a PDF file into the /srv directory
RUN wget -O /srv/bio_text_book.pdf  https://assets.openstax.org/oscms-prodcms/media/documents/ConceptsofBiology-WEB.pdf?_gl=1*1gts49r*_ga*MTA2MjY3MDcyMy4xNzA4ODkzMDUz*_ga_T746F8B0QC*MTcwODg5MzA1My4xLjAuMTcwODg5MzA1NC41OS4wLjA.

# Expose the specified port
EXPOSE $PORT

RUN export FLASK_APP="app:create_app"

# Define the default command to run the Flask application
CMD ["gunicorn", "-w", "1", "--timeout", "10000", "--reload", "-b" ,":8502", "app:create_app(testing=False)"]