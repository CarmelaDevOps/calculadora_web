# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear carpeta de logs dentro del contenedor (por si no existe)
RUN mkdir -p logs

# Exponer el puerto 5000 (Flask)
EXPOSE 5000

# Comando para correr la app
CMD ["python", "app.py"]

