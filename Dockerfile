#docker build . -t docker-dnevnic.ru
FROM python:alpine
 #создаем директорию
WORKDIR /app
 #копируем все в директорию
COPY . /app
#устанавливаем зависимости
RUN pip install -r requirements.txt

# открывает 5000 порт
EXPOSE 5000

CMD [ "python3", "main.py" ]
