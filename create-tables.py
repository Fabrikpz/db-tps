import mysql.connector
from mysql.connector import errorcode

def create_connection():
    try:
        db = mysql.connector.connect(
            host="bxkcn93dxb5qzbaf2th7-mysql.services.clever-cloud.com",
            user="ude5ew8s9zf8o1bw",
            password="zucUaOmeMxamFHXfORRJ",
            database="bxkcn93dxb5qzbaf2th7"
        )
        print("Conexión exitosa")
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está mal con tu usuario o contraseña")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(f"Error: {err}")
        return None

def create_tables(db):
    cursor = db.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
        print("Tabla 'users' creada exitosamente")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla: {err}")
    finally:
        cursor.close()

def main():
    db = create_connection()
    if db:
        create_tables(db)
        db.close()

if __name__ == "__main__":
    main()
