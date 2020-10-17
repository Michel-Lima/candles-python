# Use an official Python runtime as an image
FROM python:3.6




# Define o diretório de trabalho para seguir as instruções COPY e CMD
# Observe que não criamos um diretório com este nome - esta instrução
# cria um diretório com este nome se ele não existir
WORKDIR /code


# Instale todos os pacotes necessários especificados em requirements.txt
COPY requirement.txt /code
RUN pip install -r requirement.txt


# Executa os arquivos quando o contêiner for iniciado
COPY Conexao_DB.py /code
COPY Chamada.py /code
CMD python Chamada.py