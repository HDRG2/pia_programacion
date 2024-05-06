import psycopg2

def db_connection():
    try:
        config = {
            'host': 'localhost',
            'database': 'proyecto_papeleria',
            'port':'5432',
            'user': 'postgres',
            'password': 'postgres',
        }  
        conn = psycopg2.connect(**config)
        print("Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
    


   





    
    
    
    
    
    
    
    
    
    
