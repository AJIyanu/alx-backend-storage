-- create index for table names in column names
-- first letter only is indexed

CREATE INDEX idx_name_first ON names (LEFT(name, 1));
