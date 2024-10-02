#Usa una imagen base de Python
FROM python:3.10-slim

#Establece el directorio de trabajo en el contenedor
WORKDIR /app

#Copia los archivos de requerimientos a la imagen
COPY requirements.txt .

#Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

#Copia todo el código de la aplicación Django al directorio de trabajo del contenedor
COPY . .

#Exponer el puerto en el que correrá Django
EXPOSE 8000

#Define el comando por defecto para ejecutar cuando el contenedor se inicie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]