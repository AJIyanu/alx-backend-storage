-- ensuring comment on all lines
-- to be ddited later

SELECT band_name, split - IF(formed = NULL, 2022, formed) as lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan desc;
