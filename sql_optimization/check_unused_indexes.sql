-- AUTHOR: Sagar Gour
-- PURPOSE: Identify indexes that are taking up space but not being used by queries.
-- CONTEXT: Essential for optimizing high-throughput Postgres databases (GeneGenius/FinTech).

SELECT
    schemaname || '.' || relname AS table_name,
    indexrelname AS index_name,
    pg_size_pretty(pg_relation_size(i.indexrelid)) AS index_size,
    idx_scan AS index_scans
FROM
    pg_stat_user_indexes i
JOIN
    pg_index using (indexrelid)
WHERE
    idx_scan = 0 -- Index has NEVER been used
    AND indexrelname NOT LIKE '%pkey' -- Ignore primary keys
ORDER BY
    pg_relation_size(i.indexrelid) DESC;