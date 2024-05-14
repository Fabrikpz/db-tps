import mysql.connector

config = {
  'user': 'tu_usuario',
  'password': 'tu_contraseña',
  'host': 'direccion_del_servidor',
  'database': 'nombre_de_la_base_de_datos',
  'port': '3306' # Generalmente 3306 para MySQL
}

# Intenta establecer la conexión
try:
    conn = mysql.connector.connect(**config)
    print("Conexión establecida con la base de datos SQL en Clever Cloud.")
    # Aquí puedes realizar operaciones con la base de datos
    # Por ejemplo, ejecutar consultas SQL, insertar datos, etc.

    # No olvides cerrar la conexión cuando hayas terminado
    conn.close()
    print("Conexión cerrada.")
except mysql.connector.Error as err:
    print("Error al conectar con la base de datos: ", err)