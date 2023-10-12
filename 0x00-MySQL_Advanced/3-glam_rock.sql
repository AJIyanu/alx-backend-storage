-- list all bands in Glam rock ranked by longetivity
-- using formed and split and lifespan

SELECT band_name, IFNULL(split -  formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan desc;
