import psycopg2

def db_connection():
    try:
        config = {
            'host': 'localhost',
            'database': 'Papeleria_Proyecto',
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
    
    
def create_user():
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO EMPLEADO (idEmpleado, nombre, apPat, apMat, fecNac, curp, rfc, tel, correo, cP, calle, colonia, numExt, numInt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (1, 'JUAN', 'GALLEGOS', 'ROMERO', '1999-09-30', 'ABCD123456EFGHIJK2','ABCD123456XYZ', '5555555555', 'Juan@example.com', '12345', '123 Main St', 'Some Neighbrorhood', '1032', '1031')
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción

            print("Datos insertados correctamente")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")

def select_product(id:str):
    conn = db_connection()
    print("id" + id)
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM EMPLEADO WHERE idempleado = %s"
            cursor.execute(query,(id,))
            conn.commit()  # Confirmar la transacción
            rows = cursor.fetchone()            
            cursor.close()
            conn.close()
            print(rows)
            return rows
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")
    return None
    



   





    
    
    
    
    
    
    
    
    
    
