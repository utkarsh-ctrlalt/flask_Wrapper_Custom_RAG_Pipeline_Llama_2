# Use an official Python runtime as a parent image
FROM python:3.11-slim AS base

RUN apt-get -y update
RUN apt-get install build-essential -y
RUN apt-get install git -y
RUN apt-get install wget -y

# Set environment variables (customize as needed)
ENV APP_HOME /srv
ENV PORT 8502

# Set the working directory to /app
WORKDIR $APP_HOME

# Install any dependencies you may need (e.g., if you have non-Python dependencies)
# RUN apt-get update && apt-get install -y ...

# Copy your Python scripts and requirements file into the container

RUN git clone -b main https://github.com/utkarsh-ctrlalt/flask_Wrapper_Custom_RAG_Pipeline_Llama_2.git .
COPY requirements.txt $APP_HOME/




# Add any other scripts or resources your application needs

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN wget -O /srv/bio_text_book.pdf  https://assets.openstax.org/oscms-prodcms/media/documents/ConceptsofBiology-WEB.pdf?_gl=1*1gts49r*_ga*MTA2MjY3MDcyMy4xNzA4ODkzMDUz*_ga_T746F8B0QC*MTcwODg5MzA1My4xLjAuMTcwODg5MzA1NC41OS4wLjA.

# Expose the port that Streamlit will run on
EXPOSE $PORT
RUN export FLASK_APP="app:create_app"

# Run the Streamlit app in the background
#change the name of the script to the correct name, and then delete this line
CMD ["gunicorn", "-w", "1", "--timeout", "10000", "--reload", "-b" ,":8502", "app:create_app(testing=False)"]