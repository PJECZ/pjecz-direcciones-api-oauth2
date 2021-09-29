--
-- roles.sql
--

DROP TABLE IF EXISTS roles;

CREATE TABLE roles (
  creado datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modificado datetime DEFAULT CURRENT_TIMESTAMP,
  estatus varchar(1) NOT NULL DEFAULT 'A',
  id int(11) NOT NULL,
  nombre varchar(256) NOT NULL,
  permiso int(11) NOT NULL,
  por_defecto tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE roles
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY nombre (nombre),
  ADD KEY ix_roles_por_defecto (por_defecto);

ALTER TABLE roles
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

--
-- insertar roles
--

INSERT INTO roles (nombre, permiso) VALUES ('ADMINISTRADOR', 1);
INSERT INTO roles (nombre, permiso) VALUES ('OBSERVADOR', 1);
