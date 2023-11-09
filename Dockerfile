FROM python:bookworm
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# Update package lists for upgrades for packages that need upgrading
RUN apt-get update 
# Install GDAL library
RUN apt-get install -y --no-install-recommends gdal-bin
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]