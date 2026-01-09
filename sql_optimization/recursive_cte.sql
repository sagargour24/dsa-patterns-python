-- Recursive CTE to traverse hierarchical data (e.g., Org Charts or Comment Threads)
WITH RECURSIVE hierarchy AS (
    SELECT id, name, manager_id, 1 as level FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, h.level + 1 FROM employees e
    JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy;