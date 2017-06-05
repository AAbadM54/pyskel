# Use an official Python runtime as a base image
FROM python:3.5-slim

# Set the working directory to ./
WORKDIR ./

# Copy the current directory contents into the container at ./
ADD ./ ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install the application
RUN python setup.py install

# Run pyskel when the container launches
CMD ["rpyskel", "do_handle"]
