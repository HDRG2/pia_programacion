import psycopg2

# Conectar a la base de datos
connection = psycopg2.connect(
    dbname='Proyecto_Papeleria',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    client_encoding='UTF8'  # Especificar la codificación de caracteres adecuada
)
