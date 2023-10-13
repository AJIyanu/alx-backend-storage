-- Creates a trigger query that decreases order as new item is added
-- Updating multiple tables for one action from your application can
-- generate issue: network disconnection, crash, etc… to keep your data
-- in a good shape, let MySQL do it for you!

DELIMITER //
CREATE TRIGGER store_stock_manager
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
 --   DECLARE name VARCHAR(255);
 --   DECLARE qty INT;

  --  SELECT NEW.item_name, NEW.number INTO name, qty;

    UPDATE items
    SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
END;
//
DELIMITER ;
