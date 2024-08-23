-- Consulta 1: Estado actual de un partido entre dos colegios específicos
SELECT p.id_partido, ef1.nombre AS equipo_local, ef2.nombre AS equipo_visitante, p.resultado
FROM Partidos p
JOIN EscuelaFutbol ef1 ON p.id_equipo_local = ef1.id
JOIN EscuelaFutbol ef2 ON p.id_equipo_visitante = ef2.id
WHERE ef1.nombre = 'Monserrat' AND ef2.nombre = 'San José';

-- Consulta 2: Partidos de un deporte específico
SELECT p.id_partido, ef.nombre, p.fecha, p.resultado
FROM Partidos p
JOIN EscuelaFutbol ef ON p.id_equipo_local = ef.id OR p.id_equipo_visitante = ef.id;

-- Consulta 3: Estado actual de un Cclegio en particular
SELECT ef.nombre, ef.categoria, ef.pts
FROM EscuelaFutbol ef
WHERE ef.nombre = 'Nombre_del_Colegio';

-- Consulta 4: Datos de las compras en cantina de un producto específico
SELECT *
FROM Cantina
WHERE nombre_producto = 'Pizza';

-- Consulta 5: Información de una cancha en particular
SELECT p.id_partido, p.fecha, p.resultado, p.lugar
FROM Partidos p
WHERE p.lugar = 'Estadio Central';
