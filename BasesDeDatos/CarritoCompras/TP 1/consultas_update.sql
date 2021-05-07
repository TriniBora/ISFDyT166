---7.	Escriba una consulta SQL que permita modificar los precios de los productos marca SAMSUNG para aumentarles un 10%

UPDATE Productos
SET
	precio = precio * 1.10
WHERE
	marca = 'SAMSUNG';

---8.	Escriba una consulta SQL que permita modificar los precios de los productos marca PHILIPS para aumentarles un 15% UPDATE Productos
SET
	precio = precio * 1.15
WHERE
	marca = 'PHILIPS';

