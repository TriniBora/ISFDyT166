---1.	Listar nombre de producto y categoría para todos los productos
SELECT 
Productos.descripcion AS Producto,
Categorias.nombre AS Categoría

FROM 
	Productos

JOIN Categorias ON Productos.Categorias_id = Categorias.id

ORDER BY
	Categorias.nombre,
Productos.descripcion


---2.	Listar nombre de producto, categoría y tipo de producto para todos los productos
SELECT 
Productos.descripcion AS Producto,
Categorias.nombre AS Categoría,
Tipo_producto.nombre AS Tipo

FROM 
	Productos

JOIN Categorias ON Productos.Categorias_id = Categorias.id
JOIN Tipo_producto ON Productos.Tipo_producto_id = Tipo_producto.id

ORDER BY
	Categorias.nombre,
	Tipo_producto.nombre,
Productos.descripcion

----3.	Listar nombre de producto y categoría para todos los productos cuya categoría sea ELECTRÓNICA
SELECT 
Productos.descripcion AS Producto,
Categorias.nombre AS Categoría

FROM 
	Productos

JOIN Categorias ON Productos.Categorias_id = Categorias.id

WHERE
	Categorias.nombre = 'ELECTRÓNICA'

ORDER BY
	Categorias.nombre,
Productos.descripcion


---4.	Listar nombre de producto y categoría para todos los productos cuya categoría sea ELECTRÓNICA y cuyo precio no supere los $ 10.000,00
SELECT 
Productos.descripcion AS Producto,
Productos.precio AS Precio,
Categorias.nombre AS Categoría

FROM 
	Productos

JOIN Categorias ON Productos.Categorias_id = Categorias.id

WHERE
	Categorias.nombre = 'ELECTRÓNICA' AND Productos.precio <= 10000.00

ORDER BY
	Categorias.nombre,
	Productos.precio,
Productos.descripcion

---5.	Listar todos los productos cuyas existencias no superen las 10 unidades de la categoría ELECTRÓNICA
SELECT 
Productos.descripcion AS Producto,
Productos.existencias AS Existencias,
Categorias.nombre AS Categoría

FROM 
	Productos

JOIN Categorias ON Productos.Categorias_id = Categorias.id

WHERE
	Categorias.nombre = 'ELECTRÓNICA' AND Productos.existencias <= 10

ORDER BY
	Categorias.nombre,
	Productos.existencias,
Productos.descripcion

---6.	Listar los nombres de los productos y que estén relacionados con carritos ABANDONADOS
SELECT 
Productos.descripcion AS Producto,
Carritos.id AS Número_Carrito

FROM 
	Carritos

JOIN Productos ON Carritos.Productos_sku = Productos.sku

WHERE
	Carritos.estado = 'ABANDONADO' 

ORDER BY
Productos.descripcion

---7.	Listar los nombres de los productos y que estén relacionados con carritos ABANDONADOS y las unidades en el carrito sean mayor que 2
SELECT 
Productos.descripcion AS Producto,
Carritos.unidades AS Unidades,
Carritos.id AS Número_Carrito

FROM 
	Carritos

JOIN Productos ON Carritos.Productos_sku = Productos.sku

WHERE
	Carritos.estado = 'ABANDONADO' AND Carritos.unidades > 2

ORDER BY
Carritos.id,
Carritos.unidades,
Productos.descripcion

---8.	Listar los nombres de los clientes, su dirección y teléfono que posean carritos ACTIVOS
SELECT 
Clientes.nombre AS Cliente_nombre,
Clientes.direccion AS Cliente_domicilio,
Clientes.telefono AS Cliente_telefono

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni

WHERE
	Carritos.estado = 'ACTIVO' 

ORDER BY
Cientes.nombre

---9.	Listar los nombres de los clientes, su dirección y teléfono que posean carritos ABANDONADOS y las unidades en el carrito sean mayor que 2
SELECT 
Clientes.nombre AS Cliente_nombre,
Clientes.direccion AS Cliente_domicilio,
Clientes.telefono AS Cliente_telefono

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni

WHERE
	Carritos.estado = 'ABANDONADO' AND Carritos.unidades > 2

ORDER BY
Cientes.nombre

---10.	Listar los nombres de los clientes que hayan comprado productos de marca SAMSUNG
SELECT 
Clientes.nombre AS Cliente_nombre

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni
JOIN Productos ON Carritos.Productos_sku = Productos.sku


WHERE
	Productos.marca = 'SAMSUNG' AND Carritos.estado <> 'ABANDONADO'

ORDER BY
Clientes.nombre

---11.	Listar los nombres de los clientes y de los productos, que hayan comprado productos de marca PHILIPS
SELECT 
Clientes.nombre AS Cliente_nombre,
Productos.descripcion AS Producto

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni
JOIN Productos ON Carritos.Productos_sku = Productos.sku


WHERE
	Productos.marca = 'PHILIPS' AND Carritos.estado <> 'ABANDONADO'

ORDER BY
Clientes.nombre,
Productos.descripcion

---12.	Listar los nombres de los clientes y de los productos, que hayan comprado productos de marca PHILIPS y su precio sea menor a $ 10.000,00
SELECT 
Clientes.nombre AS Cliente_nombre,
Productos.descripcion AS Producto

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni
JOIN Productos ON Carritos.Productos_sku = Productos.sku


WHERE
	Productos.marca = 'PHILIPS' AND Carritos.estado <> 'ABANDONADO' AND Productos.precio < 10000.00

ORDER BY
Clientes.nombre,
Productos.descripcion

---13.	Obtener por cada carrito el costo total, que se obtiene de multiplicar las unidades del carrito con el precio del producto relacionado
SELECT 
	Carritos.id AS Id_Carrito,
	Carritos.unidades AS Unidades_Carrito,	
	Productos.precio AS Precio_Producto,
	Productos.precio*Carritos.unidades AS Costo_Total

FROM
	Carritos

JOIN Productos ON Carritos.Productos_sku = Productos.sku

ORDER BY
Carritos.id


---14.	Seleccionar los nombre de los clientes que hayan ABANDONADO carritos con productos de marca SAMSUNG y cuyo tipo de producto sea ELECTRODOMÉSTICO
SELECT 
Clientes.nombre AS Cliente_nombre

FROM 
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni
JOIN Productos ON Carritos.Productos_sku = Productos.sku
JOIN Tipo_producto ON Productos.Tipo_producto_id = Tipo_producto.id


WHERE
	Productos.marca = 'SAMSUNG' AND Carritos.estado = 'ABANDONADO' AND Tipo_producto.nombre = 'ELECTRODOMÉSTICO'

ORDER BY
Clientes.nombre

---15.	Listar los datos completos de los clientes que hayan gastado mas de $ 5.000,00 por carrito, donde el total del carrito se calcula haciendo las unidades del carrito por el precio del producto seleccionado
SELECT 
	Clientes.dni AS DNI_Cliente,
	Clientes.nombre AS Nombre_Cliente,
	Clientes.direccion AS Domicilio_Cliente,
	Clientes.telefono AS Telefono_Cliente,
	Productos.precio*Carritos.unidades AS Costo_Total


FROM
	Carritos

JOIN Clientes ON Carritos.Clientes_dni = Clientes.dni
JOIN Productos ON Carritos.Productos_sku = Productos.sku

WHERE 
Productos.precio*Carritos.unidades > 5000.00 AND Carritos.estado <> 'ABANDONADO'

ORDER BY
Clientes.nombre
