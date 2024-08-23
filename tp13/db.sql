CREATE TABLE EscuelaFutbol (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    pts INT NOT NULL,
    pj INT NOT NULL,
    pg INT NOT NULL,
    pp INT NOT NULL,
    gf INT NOT NULL,
    gc INT NOT NULL,
    dg INT NOT NULL,
    categoria VARCHAR(20) NOT NULL
);

CREATE TABLE EscuelaVoley (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    pts INT NOT NULL,
    pj INT NOT NULL,
    pg INT NOT NULL,
    pp INT NOT NULL,
    gf INT NOT NULL,
    gc INT NOT NULL,
    dg INT NOT NULL,
    categoria VARCHAR(20) NOT NULL
);

CREATE TABLE EscuelaBasquet (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    pts INT NOT NULL,
    pj INT NOT NULL,
    pg INT NOT NULL,
    pp INT NOT NULL,
    gf INT NOT NULL,
    gc INT NOT NULL,
    dg INT NOT NULL,
    categoria VARCHAR(20) NOT NULL
);

CREATE TABLE Cantina (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
);
