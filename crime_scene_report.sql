SELECT * FROM crime_scene_report
WHERE type = 'murder' AND date = 20180115 AND city = 'SQL City'

SELECT * FROM person
WHERE address_street_name = "Northwestern Dr" ORDER BY address_number desc

SELECT * FROM interview
WHERE person_id = 14887

SELECT * FROM get_fit_now_member
WHERE membership_status = 'gold' AND id like '48Z%'

SELECT * FROM drivers_license
WHERE plate_number like '%H42W%'

SELECT * FROM person
WHERE license_id like 183779 OR license_id like 423327 OR license_id like 664760

SELECT * FROM interview
WHERE person_id like 67318