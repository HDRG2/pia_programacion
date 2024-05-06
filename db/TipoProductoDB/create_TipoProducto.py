from db.conexion import db_connection

def create_TipoProducto(new_tipoproducto):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO TIPOPRODUCTO (idTipoProducto,descr)
            VALUES (%s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (int(new_tipoproducto['ID']), new_tipoproducto['descripcion'])
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción
            cursor.close()
            conn.close()
            
            return "Datos insertados correctamente"
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")