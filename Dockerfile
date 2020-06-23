FROM python:3.7


ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /BTCwebhook
WORKDIR /BTCwebhook
COPY . /BTCwebhook

# Installing requirements
ADD requirements/requirements.txt /BTCwebhook
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

## Collect static files
#RUN python manage.py collectstatic --no-input
#RUN python manage.py shell
#
#CMD ["gunicorn", "--chdir", "BTCwebhook", "--bind", ":8000", "BTCwebhook.wsgi:application"]
