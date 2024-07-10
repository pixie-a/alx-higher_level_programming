-- Lists all records of the table second_table having a name value in my MySQL server.
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;

