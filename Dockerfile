#docker build . -t docker-dnevnic.ru && docker run -d docker-dnevnic.ru && docker update --restart unless-stopped docker-dnevnic.ru

FROM python:alpine
 #создаем директорию
WORKDIR /app
 #копируем все в директорию
COPY . /app
#устанавливаем зависимости
RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
