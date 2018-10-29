# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/d20/src
WORKDIR /opt/services/d20/src

# install our dependencies
ADD requirements.txt /opt/services/d20/src
RUN pip install -r requirements.txt

# copy and prepare our project code
COPY . /opt/services/d20/src
RUN cd d20 && python manage.py collectstatic --no-input

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "mimir", "--bind", ":8000", "mimir.wsgi:application"]