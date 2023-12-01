

SELECT id 
FROM Weather 
WHERE temperature > (
    SELECT temperature 
    FROM Weather as Compare 
    WHERE Compare.recordDate = Weather.recordDate - INTERVAL 1 DAY
    AND Compare.temperature < Weather.Temperature
)
