from db.conexion import db_connection

def mostrar_TipoProducto(id:str):
    conn = db_connection()
    print("id" + id)
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT idTipoProducto, descripsion FROM TIPOPRODUCTO"
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
    