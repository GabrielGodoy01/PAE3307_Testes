FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest"]

# Para construir imagem:
    # docker build -t nome-projeto .

# Para rodar o projeto
    # docker run nome-projeto