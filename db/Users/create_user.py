from db.conexion import db_connection

def create_user(new_user):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO EMPLEADO (idEmpleado, nombre, apPat, apMat, fecNac, curp, rfc, tel, correo, cP, calle, colonia, numExt, numInt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (new_user['id'], new_user['name'], 'GALLEGOS', 'ROMERO', '1999-09-30', 'ABCD123456EFGHIJK2','ABCD123456XYZ', '5555555555', 'Juan@example.com', '12345', '123 Main St', 'Some Neighbrorhood', '1032', '1031')
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción

            print("Datos insertados correctamente")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")