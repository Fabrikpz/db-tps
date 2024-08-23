from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

username = 'ude5ew8s9zf8o1bw'
password = 'zucUaOmeMxamFHXfORRJ'
hostname = 'bxkcn93dxb5qzbaf2th7-mysql.services.clever-cloud.com'
database = 'bxkcn93dxb5qzbaf2th7'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cantina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_venta = db.Column(db.Date, nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()