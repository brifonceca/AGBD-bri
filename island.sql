SELECT * FROM village 
-- Select: Para seleccionar
-- *: Todos
-- From:De donde 

SELECT * FROM INHABITANT 
-- Inhabitant: Un habitante 

SELECT * FROM INHABITANT WHERE state = "friendly" 
-- Where: Donde 
-- State: En este caso seria el estado de ciertos habitantes 

SELECT * FROM INHABITANT WHERE job LIKE "weaponsmith" and state = "friendly"
-- Job: Trabajo
-- Like: Sirve cuando no sabemos si algo es exacto con algo y su vez nos permite utilizar el % 

SELECT * FROM INHABITANT WHERE job LIKE "%smith" and state = "friendly"
-- % Al principo termina
-- Atras comienza %
-- Contiene es con % (al principio y al final)

SELECT personid FROM INHABITANT WHERE name = 'Stranger'
-- Personid: Identidad de los habitantes

SELECT gold FROM INHABITANT WHERE name = 'Stranger' 
-- Gold: Oro

SELECT * FROM ITEM WHERE OWNER IS NULL 
-- Item: Objetos
-- Owner: Propietario

UPDATE item SET owner = 20 WHERE owner IS NULL 
-- Update: Actualizar a quien le damos el objeto
-- Set: Establece 

SELECT * FROM ITEM WHERE owner = 20

SELECT * FROM INHABITANT WHERE state = "friendly" and job = "dealer" or job = "merchant"

UPDATE item set owner = 15

UPDATE INHABITANT SET name = "patito" where personid =20

SELECT * FROM INHABITANT where job = "baker" ORDER BY gold DESC

SELECT * FROM INHABITANT where job = "pilot"

SELECT name FROM inhabitant WHERE personid = 13

SELECT COUNT(*) FROM inhabitant, village
WHERE village.villageid = inhabitant.villageid AND village.name = 'Onionville' AND inhabitant.gender = "f"
-- COUNT: Cuenta todos los habitantes de la isla

SELECT inhabitant.name FROM inhabitant, village 
WHERE village.villageid = inhabitant.villageid AND village.name = 'Onionville' AND inhabitant.gender = "f"

SELECT SUM(inhabitant.gold) FROM inhabitant WHERE job = 'baker' OR job = 'dealer' OR job = 'merchant'
-- SUM: Suma todo el oro de los habitantes 

SELECT state, AVG(inhabitant.gold) FROM inhabitant
GROUP BY state ORDER BY AVG(inhabitant.gold)
-- AVG: Calcula el oro promedio de los habitantes

DELETE FROM inhabitant WHERE name LIKE 'dirty diane' 
-- Delete:  En este caso borra al personaje 

update inhabitant SET state = 'friendly' where job = 'pilot'


