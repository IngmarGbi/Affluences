-- USE `test_technique`;
-- timetables query
SELECT ti.site_id, 
		CONCAT(ti.opening_day,' ',ti.opening_time) 'opening_datetime',
		CONCAT(ti.closing_day,' ',ti.closing_time) 'closing_datetime'
FROM timetables ti
WHERE 1=1
AND opening_day = '2021-05-06'
AND closing_day = '2021-05-06'
AND opening_time IS NOT NULL
AND closing_time IS NOT NULL
ORDER BY ti.site_id
;