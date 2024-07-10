-- This an SQL script that ranks country origins of bands, ordered by the number of (n-- on-unique) fans

SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;