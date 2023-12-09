# Используйте официальный образ Python с вашей версией Python
FROM python:3.11

# Установите переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /main
WORKDIR /main
#COPY requirements.txt /main
COPY . /main/
RUN pip install -r /main/requirements.txt

#CMD ["python", "/main/manage.py", "migrate"]
CMD ["python", "/main/manage.py", "runserver", "0.0.0.0:8000"]
