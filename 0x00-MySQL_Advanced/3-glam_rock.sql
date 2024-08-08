-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
CREATE VIEW country_fan_count AS
SELECT 
    origin, 
    SUM(fans) AS nb_fans
FROM 
    bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;

-- Select the results from the view
SELECT 
    origin, 
    nb_fans
FROM 
    country_fan_count;
