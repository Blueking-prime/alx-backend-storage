-- a script that bands by countries
-- Lists bands
   SELECT `band_name` AS band_name,
CASE WHEN split IS NULL THEN (2020 - formed)
     ELSE (split - formed) END AS lifespan
     FROM metal_bands
    WHERE style LIKE '%Glam rock%'
 ORDER BY lifespan DESC, band_name DESC;
