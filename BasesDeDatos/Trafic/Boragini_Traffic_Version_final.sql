-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-02-04 14:57:08.518

-- tables
-- Table: empresas
CREATE TABLE empresas (
    nombre_usuario varchar(15)  NOT NULL,
    nombre_real varchar(40)  NOT NULL,
    domicilio varchar(50)  NULL,
    localidad varchar(40)  NULL,
    cuit varchar(13)  NOT NULL,
    telefono varchar(20)  NOT NULL,
    mail varchar(40)  NOT NULL,
    avatar varchar(20)  NOT NULL,
    CONSTRAINT mail_valido CHECK (mail ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$') NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT empresas_pk PRIMARY KEY (nombre_usuario)
);

-- Table: estados_usuario
CREATE TABLE estados_usuario (
    id varchar(1)  NOT NULL,
    descripcion varchar(20)  NOT NULL,
    CONSTRAINT estados_usuario_pk PRIMARY KEY (id)
);

-- Table: posiciones_historico
CREATE TABLE posiciones_historico (
    fecha_hora timestamp  NOT NULL,
    usuarios_nombre_usuario varchar(10)  NOT NULL,
    latitud decimal(8,5)  NOT NULL,
    longitud decimal(8,5)  NOT NULL,
    CONSTRAINT latitud_valida CHECK (latitud >= -90.0 AND latitud <= 90.0) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT longitud_valida CHECK (longitud >= -180.0 AND longitud <= 180.0) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT posiciones_historico_pk PRIMARY KEY (fecha_hora,usuarios_nombre_usuario)
);

-- Table: tipos_usuario
CREATE TABLE tipos_usuario (
    id varchar(1)  NOT NULL,
    descripcion varchar(20)  NOT NULL,
    CONSTRAINT tipos_usuario_pk PRIMARY KEY (id)
);

-- Table: usuarios
CREATE TABLE usuarios (
    nombre_usuario varchar(10)  NOT NULL,
    nombre_real varchar(40)  NOT NULL,
    dni varchar(8)  NOT NULL,
    domicilio varchar(50)  NULL,
    localidad varchar(40)  NULL,
    telefono varchar(20)  NOT NULL,
    mail varchar(40)  NOT NULL,
    avatar varchar(20)  NOT NULL,
    tipos_usuario_id varchar(1)  NOT NULL,
    estados_usuario_id varchar(1)  NOT NULL,
    CONSTRAINT mail_valido CHECK (mail ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$') NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT usuarios_pk PRIMARY KEY (nombre_usuario)
);

-- Table: usuarios_corporativos
CREATE TABLE usuarios_corporativos (
    usuarios_nombre_usuario varchar(10)  NOT NULL,
    empresas_nombre_usuario varchar(15)  NOT NULL,
    CONSTRAINT usuarios_corporativos_pk PRIMARY KEY (usuarios_nombre_usuario,empresas_nombre_usuario)
);

-- foreign keys
-- Reference: posiciones_historico_usuarios (table: posiciones_historico)
ALTER TABLE posiciones_historico ADD CONSTRAINT posiciones_historico_usuarios
    FOREIGN KEY (usuarios_nombre_usuario)
    REFERENCES usuarios (nombre_usuario)  
    ON UPDATE CASCADE --si se modifica el nombre_usuario se actualiza en esta tabla
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
    
;

-- Reference: usuarios_corporativos_empresas (table: usuarios_corporativos)
ALTER TABLE usuarios_corporativos ADD CONSTRAINT usuarios_corporativos_empresas
    FOREIGN KEY (empresas_nombre_usuario)
    REFERENCES empresas (nombre_usuario)  
    ON DELETE CASCADE -- si se modifica/elimina el nombre_empresa se actualiza/elimina de esta tabla
    ON UPDATE CASCADE
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: usuarios_corporativos_usuarios (table: usuarios_corporativos)
--ALTER TABLE usuarios_corporativos ADD CONSTRAINT usuarios_corporativos_usuarios
ALTER TABLE usuarios_corporativos ADD CONSTRAINT usuarios_corporativos_usuarios
    FOREIGN KEY (usuarios_nombre_usuario)
    REFERENCES usuarios (nombre_usuario)  
    ON DELETE CASCADE -- si se modifica/elimina el nombre_usuario o el usuario deja de ser corporativo se actualiza/elimina de esta tabla
    ON UPDATE CASCADE
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
    ;

-- Reference: usuarios_estados_usuario (table: usuarios)
ALTER TABLE usuarios ADD CONSTRAINT usuarios_estados_usuario
    FOREIGN KEY (estados_usuario_id)
    REFERENCES estados_usuario (id)  
    ON UPDATE CASCADE --actualiza si se modifica estados_usuario
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: usuarios_tipos_usuario (table: usuarios)
ALTER TABLE usuarios ADD CONSTRAINT usuarios_tipos_usuario
    FOREIGN KEY (tipos_usuario_id)
    REFERENCES tipos_usuario (id)  
    ON UPDATE CASCADE --actualiza si se modifica tipos_usuario
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

