--
-- estados
--

DROP TABLE IF EXISTS estados;

CREATE TABLE estados (
  creado datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modificado datetime DEFAULT CURRENT_TIMESTAMP,
  estatus varchar(1) NOT NULL DEFAULT 'A',
  id int(11) NOT NULL,
  nombre varchar(256) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE estados
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY ix_nombre (nombre);

ALTER TABLE estados
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;


INSERT INTO estados (nombre) VALUES ('Aguascalientes');
INSERT INTO estados (nombre) VALUES ('Baja California');
INSERT INTO estados (nombre) VALUES ('Baja California Sur');
INSERT INTO estados (nombre) VALUES ('Campeche');
INSERT INTO estados (nombre) VALUES ('Chiapas');
INSERT INTO estados (nombre) VALUES ('Chihuahua');
INSERT INTO estados (nombre) VALUES ('Coahuila de Zaragoza');
INSERT INTO estados (nombre) VALUES ('Colima');
INSERT INTO estados (nombre) VALUES ('Durango');
INSERT INTO estados (nombre) VALUES ('Guanajuato');
INSERT INTO estados (nombre) VALUES ('Guerrero');
INSERT INTO estados (nombre) VALUES ('Hidalgo');
INSERT INTO estados (nombre) VALUES ('Jalisco');
INSERT INTO estados (nombre) VALUES ('Estado de México');
INSERT INTO estados (nombre) VALUES ('Michoacán de Ocampo');
INSERT INTO estados (nombre) VALUES ('Morelos');
INSERT INTO estados (nombre) VALUES ('Nayarit');
INSERT INTO estados (nombre) VALUES ('Nuevo');
INSERT INTO estados (nombre) VALUES ('Oaxaca');
INSERT INTO estados (nombre) VALUES ('Puebla');
INSERT INTO estados (nombre) VALUES ('Querétaro');
INSERT INTO estados (nombre) VALUES ('Quintana Roo');
INSERT INTO estados (nombre) VALUES ('San Luis Potosí');
INSERT INTO estados (nombre) VALUES ('Sinaloa');
INSERT INTO estados (nombre) VALUES ('Sonora');
INSERT INTO estados (nombre) VALUES ('Tabasco');
INSERT INTO estados (nombre) VALUES ('Tamaulipas');
INSERT INTO estados (nombre) VALUES ('Tlaxcala');
INSERT INTO estados (nombre) VALUES ('Veracruz de Ignacio de la Llave');
INSERT INTO estados (nombre) VALUES ('Yucatán');
INSERT INTO estados (nombre) VALUES ('Zacatecas');
