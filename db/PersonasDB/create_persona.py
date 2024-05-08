from db.conexion import db_connection
from utilities.generate_id import generate_id

def create_persona(new_persona):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO PERSONA (idPersona, nombre, apPat, apMat, fecNac, curp, rfc, tel, correo  )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (generate_id(), new_persona['Nombre'], new_persona['ApPat'], new_persona['ApMat'], new_persona['FecNac'], new_persona['curp'], new_persona['rfc'], new_persona['telefono'], new_persona['correo'] )
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción
            cursor.close()
            conn.close()
            
            return "Datos insertados correctamente"
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")