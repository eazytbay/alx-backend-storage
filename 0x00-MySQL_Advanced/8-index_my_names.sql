-- This is a Script that creates an index idx_name_first on
-- names of the tablet and the first letter of name.
CREATE INDEX idx_name_first ON names(name(1))
