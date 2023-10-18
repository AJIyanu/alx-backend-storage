-- create index for table names in column names
-- first letter only is indexed

-- ALTER TABLE names ADD COLUMN idx_first CHAR(1);
-- UPDATE names SET idx_first = LEFT(name, 1);
CREATE INDEX idx_name_first2 ON names ((LEFT(name, 1)));
