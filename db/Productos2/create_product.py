from db.conexion import db_connection

def create_product(new_products):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO PRODUCTOS (idProducto, nomProducto, precio, existencia, idTipoProducto)
            VALUES (%s, %s, %s, %s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (new_products['id'], new_products['name'], '', 'ROMERO', '1999-09-30', 'ABCD123456EFGHIJK2')
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción

            print("Datos insertados correctamente")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")