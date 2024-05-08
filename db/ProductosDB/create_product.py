from db.conexion import db_connection
from utilities.generate_id import generate_id
def create_product(new_product):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """INSERT INTO PRODUCTO (idProducto, nomProducto, precio, existencia, idTipoProducto)
            VALUES (%s, %s, %s, %s, %s)"""
            # Aquí proporciona los valores que deseas insertar
            values = (generate_id(), new_product['name'],float(new_product['precio']),int(new_product['existencia']), int(new_product['TipoProducto']))
            cursor.execute(query, values)
            conn.commit()  # Confirmar la transacción
            cursor.close()
            conn.close()
            
            return "Datos insertados correctamente"
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
    else:
        print("No se pudo establecer la conexión con la base de datos")