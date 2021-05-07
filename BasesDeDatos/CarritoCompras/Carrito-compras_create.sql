-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-10-22 22:07:12.05

-- tables
-- Table: Carritos
CREATE TABLE Carritos (
    sku int  NOT NULL,
    unidades int  NOT NULL,
    estado varchar(10)  NOT NULL,
    Clientes_dni bigint  NOT NULL,
    Productos_sku int  NOT NULL,
    CONSTRAINT Carritos_pk PRIMARY KEY (sku)
);

-- Table: Categorias
CREATE TABLE Categorias (
    id int  NOT NULL,
    nombre varchar(30)  NOT NULL,
    CONSTRAINT Categorias_pk PRIMARY KEY (id)
);

-- Table: Clientes
CREATE TABLE Clientes (
    dni bigint  NOT NULL,
    nombre varchar(70)  NOT NULL,
    telefono varchar(15)  NOT NULL,
    direccion varchar(40)  NOT NULL,
    tarjetas varchar(15)  NOT NULL,
    CONSTRAINT Clientes_pk PRIMARY KEY (dni)
);

-- Table: Productos
CREATE TABLE Productos (
    sku int  NOT NULL,
    descripcion varchar(70)  NOT NULL,
    marca varchar(30)  NOT NULL,
    precio decimal(10,2)  NOT NULL,
    Categorias_id int  NOT NULL,
    Tipo_productos_id int  NOT NULL,
    CONSTRAINT Productos_pk PRIMARY KEY (sku)
);

-- Table: Tipo_productos
CREATE TABLE Tipo_productos (
    id int  NOT NULL,
    nombre varchar(30)  NOT NULL,
    CONSTRAINT Tipo_productos_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: Carritos_Clientes (table: Carritos)
ALTER TABLE Carritos ADD CONSTRAINT Carritos_Clientes
    FOREIGN KEY (Clientes_dni)
    REFERENCES Clientes (dni)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Carritos_Productos (table: Carritos)
ALTER TABLE Carritos ADD CONSTRAINT Carritos_Productos
    FOREIGN KEY (Productos_sku)
    REFERENCES Productos (sku)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Productos_Categorias (table: Productos)
ALTER TABLE Productos ADD CONSTRAINT Productos_Categorias
    FOREIGN KEY (Categorias_id)
    REFERENCES Categorias (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Productos_Tipo_productos (table: Productos)
ALTER TABLE Productos ADD CONSTRAINT Productos_Tipo_productos
    FOREIGN KEY (Tipo_productos_id)
    REFERENCES Tipo_productos (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

