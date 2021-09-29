--
-- usuarios
--

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
  creado datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modificado datetime DEFAULT CURRENT_TIMESTAMP,
  estatus varchar(1) NOT NULL DEFAULT 'A',
  id int(11) NOT NULL,
  rol_id int(11) NOT NULL,
  email varchar(256) DEFAULT NULL,
  contrasena varchar(256) NOT NULL,
  nombres varchar(256) NOT NULL,
  apellido_paterno varchar(256) NOT NULL,
  apellido_materno varchar(256) DEFAULT NULL,
  telefono_celular varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE usuarios
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY ix_usuarios_email (email),
  ADD KEY ix_usuarios_rol_id (rol_id);

ALTER TABLE usuarios
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE usuarios
  ADD CONSTRAINT usuarios_ibfk_1 FOREIGN KEY (rol_id) REFERENCES roles (id);

--
-- insertar usuarios
--

INSERT INTO usuarios (rol_id, email, contrasena, nombres, apellido_paterno, apellido_materno)
  VALUES (1, 'guillermo.valdes@pjecz.gob.mx', '$pbkdf2-sha256$29000$CcEYgxCCsDbmvDfGuFdKaQ$fzCyDQIT3q/j50HUHQR3MeC.BgSW1z1y7obEkUHvIds', 'Guillermo', 'Valdes', 'Lozano');
