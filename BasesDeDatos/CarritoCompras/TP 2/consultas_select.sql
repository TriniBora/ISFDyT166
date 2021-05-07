---1.	Seleccionar todos los clientes ordenados alfabéticamente

SELECT *
FROM Clientes

ORDER BY nombre

---(por defecto los ordena en forma ascendente)


---2.	Seleccionar todos los productos ordenados alfabéticamente

SELECT *
FROM Productos

ORDER BY descripcion

---(por defecto los ordena en forma ascendente)

---3.	Seleccionar todos los productos cuyas existencias sean menores a 10 unidades

SELECT *
FROM Productos

WHERE
	existencias < 10

ORDER BY existencias

---(por defecto los ordena en forma ascendente)

---4.	Seleccionar todos los productos cuya marca sea SAMSUNG
SELECT *
FROM Productos

WHERE
	marca = 'SAMSUNG'

ORDER BY descripcion

---(por defecto los ordena en forma ascendente)

---5.	Seleccionar todos los productos cuya marca sea SAMSUNG y la cantidad de existencias sea menor a 10 unidades
SELECT *
FROM Productos

WHERE
	marca = 'SAMSUNG' AND existencias < 10

ORDER BY descripcion

---(por defecto los ordena en forma ascendente)

---6.	Seleccionar todos los productos cuya marca sea SAMSUNG o PHILIPS
SELECT *
FROM Productos

WHERE
	marca = 'SAMSUNG' OR marca = 'PHILIPS'

ORDER BY marca, descripcion

---(por defecto los ordena en forma ascendente, primero por marca, luego por descripción)

---7.	Seleccionar todos las Categorías que cuyo nombre comiencen con "Elec"
SELECT *
FROM Categorias

WHERE
	nombre LIKE 'ELEC%'

---8.	Seleccionar todos los carritos que dispongan más de 3 unidades
SELECT *
FROM Carritos

WHERE
	Unidades > 3

ORDER BY unidades, estado
---(por defecto los ordena en forma ascendente, primero por unidades, luego por estado)

---9.	Seleccionar todos los carritos en estado ABANDONADO
SELECT *
FROM Carritos

WHERE
	estado = 'ABANDONADO'

---10.	Seleccionar todos los clientes con tarjeta VISA
SELECT *
FROM Clientes

WHERE
	tarjetas = 'VISA'

---11.	Seleccionar todos los clientes con apellido Rodriguez
SELECT *
FROM Clientes

WHERE
	nombre = 'Rodriguez'

---12.	Seleccionar todos los clientes cuyo DNI sea mayor a 25 millones y menor a 30 millones
SELECT *
FROM Clientes

WHERE
	dni > 25000000 AND dni < 30000000

---13.	Seleccionar a todos los clientes cuya característica telefónica sea de la ciudad de Tandil
SELECT *
FROM Clientes

WHERE
	Telefono LIKE '0249%'
VER OTRAS POSIBILIDADES

---14.	Seleccionar todos los carritos con estado ACTIVO y con menos de 5 unidades

SELECT *
FROM Carritos

WHERE
	estado = 'ACTIVO' AND unidades < 5
