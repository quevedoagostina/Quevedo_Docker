# Usa la imagen base de Python 3.11
FROM python:3.11

# Establece wel directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expón el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app/app.py"]

