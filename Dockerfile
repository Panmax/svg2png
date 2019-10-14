FROM python:3.6

#RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list && rm -Rf /var/lib/apt/lists/* && apt-get update
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

ADD pip.conf ~/.pip/pip.conf

# Add requirements.txt
ADD requirements.txt /webapp/requirements.txt

# Install gunicorn Python web server
RUN pip install gunicorn==19.9.0
# Install app requirements
RUN pip install -r /webapp/requirements.txt

# Create app directory
ADD . /webapp

# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp

# Expose port 5000 for gunicorn
EXPOSE 5000

ENTRYPOINT ["gunicorn", "-w", "2", "wsgi:app", "-b", "0.0.0.0:5000", "-n", "docker-flask", "--timeout", "45", "--max-requests", "10000"]