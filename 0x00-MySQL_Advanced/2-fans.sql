-- ensuring comment on all line
-- to be ddited later

-- SELECT origin, fans, rank() OVER(partition by origin order by fans desc) AS 'nb_fans' FROM  metal_bands;

SELECT origin, SUM(fans) as 'nb_fans' from metal_bands GROUP BY origin
ORDER BY nb_fans desc;
