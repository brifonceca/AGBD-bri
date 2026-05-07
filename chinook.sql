-- Ejercicio 1
SELECT FirstName, LastName FROM employees ORDER BY FirstName ASC
-- Order by: Utilizado parsa organizar los elementos
-- ASC: Es para medir del más chico al más grande


-- Ejercicio 2
SELECT * FROM albums, tracks WHERE Title = "Big Ones"
ORDER BY Milliseconds DESC
-- DESC: Mide desde el más grande al más chico


-- Ejercicio 3
SELECT Title, sum(UnitPrice) FROM tracks
JOIN albums ON tracks.AlbumId = albums.AlbumId
GROUP BY tracks.AlbumId ORDER BY UnitPrice ASC LIMIT 10
-- Sum: Permite la suma de los elementos
-- Join: Permite combinar filas (On también viene con el join)
-- Group by: Agrupa filas
-- Limit ...: Habilita el limite de los elementos que queremos visualizar


-- Ejercicio 4
SELECT t.name AS cancion,g.name AS genero, a.Title AS albums_title, t.UnitPrice FROM tracks t
JOIN genres g ON t.GenreId = g.GenreId
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE t.UnitPrice = 0.99
-- As: Renombra columnas
-- From:
-- Where: Donde tal cosa haga tal cosa


-- Ejercicio 5
SELECT t.name AS cancion,t.Milliseconds AS duracion, a.Title AS album, ar.name AS artist
FROM tracks t JOIN albums a ON a.AlbumId = t.AlbumId
JOIN artists ar ON ar.ArtistId = a.ArtistId
ORDER BY t.Milliseconds ASC LIMIT 20


-- Ejercicio 6
SELECT emp.LastName AS apellidos, emp.Title AS puesto, jef.LastName AS apellidoJef, COUNT (*) AS cant_clientes
FROM employees emp JOIN employees jef ON emp.ReportsTo = jef.EmployeeId
JOIN customers c ON c.SupportRepId = emp.EmployeeId
GROUP BY emp.EmployeeId ORDER BY cant_clientes DESC


-- Ejercicio 7
SELECT emp.FirstName AS Nombre_emp, emp.LastName As Apellido_emp, c.FirstName AS Nombre_cli, c.LastName As Apellido_cli
FROM employees emp JOIN customers c


-- Ejercicio 8
SELECT c.FirstName AS Nombre_cli, c.LastName As Apellido_cli, c.Address AS Direccion_cli, i.InvoiceDate AS Factura
FROM customers c JOIN invoices i


-- Ejercicio 9
SELECT g.name As Genero, sum (t.GenreId) As Canciones
FROM genres g JOIN tracks t WHERE g.GenreId = t.GenreId
GROUP BY g.name ORDER BY Canciones DESC

-- Ejercicio 10
SELECT c.FirstName AS Nombre_cli, ar.name AS Artista_nom
FROM customers c 
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN albums al ON t.AlbumId = al.AlbumId
JOIN artists ar ON al.ArtistId = ar.ArtistId
GROUP BY c.FirstName, ar.name 

-- Ejercicio 11
SELECT c.FirstName AS Nombre_cli, c.City AS Direccion, t.name AS Cancion, g.name AS Genero
FROM customers c 
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN genres g ON t.GenreId = g.GenreId

-- Ejercicio 12
SELECT * FROM employees e 
JOIN customers c ON e.EmployeeId = c.SupportRepId 
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN albums al ON t.AlbumId = al.AlbumId
JOIN artists ar ON al.ArtistId = ar.ArtistId
JOIN genres g ON t.GenreId = g.GenreId
JOIN media_types mp ON t.MediaTypeId = mp.MediaTypeId
JOIN playlist_track pt ON t.TrackId = pt.TrackId
JOIN playlists p ON pt.PlaylistId = p.PlaylistId
