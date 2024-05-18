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

def insert_user(db, username, email):
    if db:
        cursor = db.cursor()
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        val = (username, email)
        try:
            cursor.execute(sql, val)
            db.commit()
            print(cursor.rowcount, "registro insertado.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
    else:
        print("No se puede insertar usuario sin conexión a la base de datos")

def get_users(db):
    if db:
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
    else:
        print("No se pueden obtener usuarios sin conexión a la base de datos")

def delete_user(db, user_id):
    if db:
        cursor = db.cursor()
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        try:
            cursor.execute(sql, val)
            db.commit()
            print(cursor.rowcount, "registro eliminado.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
    else:
        print("No se puede eliminar usuario sin conexión a la base de datos")

def menu():
    db = create_connection()
    while True:
        print("1. Insertar usuario.")
        print("2. Mostrar usuarios.")
        print("3. Eliminar usuario.")
        print("4. Salir.")
        choice = input("Elige una opción: ")
        if choice == '1':
            username = input("Escribe nombre de usuario: ")
            email = input("Escribe email: ")
            insert_user(db, username, email)
        elif choice == '2':
            get_users(db)
        elif choice == '3':
            user_id = input("Escribe la ID del usuario a eliminar: ")
            delete_user(db, user_id)
        elif choice == '4':
            if db:
                db.close()
            break

if __name__ == "__main__":
    menu()