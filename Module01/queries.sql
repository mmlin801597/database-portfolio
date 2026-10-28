SELECT machine, COUNT(*) AS total_readings
FROM readings
GROUP BY machine
ORDER BY machine;

SELECT machine, ROUND(AVG(spindle_load), 2) AS average_load
FROM readings
GROUP BY machine
ORDER BY average_load DESC;