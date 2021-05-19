-- USE `test_technique`;
-- Data Query
 SELECT re.sensor_id 'sensor_identifier',se.sensor_name 'sensor_name',sen_se.site_id 'site_id',max(re.record_datetime) 'last_record_datetime'
FROM records re
LEFT JOIN sensors se on re.sensor_id = se.sensor_id
LEFT JOIN sensors_settings sen_se on re.sensor_id = sen_se.sensor_id
-- Filtre sur les sites NULL dès maintenant pour accélérer la requête
WHERE sen_se.site_id is not NULL
GROUP BY re.sensor_id;
