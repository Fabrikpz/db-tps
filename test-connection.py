import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="bxkcn93dxb5qzbaf2th7-mysql.services.clever-cloud.com",
        user="ude5ew8s9zf8o1bw",
        password="zucUaOmeMxamFHXfORRJ",
        database="bxkcn93dxb5qzbaf2th7"
    )

def main():
    try:
        # Conectarse a la base de datos
        db_connection = connect_to_database()
        
        if db_connection.is_connected():
            print("Conexión exitosa a la base de datos en Clever Cloud")
            
            # Realizar las operaciones que necesites aquí
            
    except mysql.connector.Error as err:
        print("Error al conectarse a la base de datos: {}".format(err))

if __name__ == "__main__":
    main()