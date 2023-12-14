-- 1 --------------------------------------------
USE solar_bd;

DROP TRIGGER IF EXISTS before_insert_order;

DELIMITER //

CREATE TRIGGER before_insert_order
BEFORE INSERT ON `solar_bd`.`order`
FOR EACH ROW
BEGIN
	DECLARE delivery_count INT;
    SELECT COUNT(*) INTO delivery_count FROM `solar_bd`.`delivery` WHERE `id` = NEW.`delivery_id`;

    IF delivery_count = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'DELIVERY OUT FROM THIS GALAXY';
	END IF;
END//

DELIMITER ;
-- -----------------------------------------------

-- 3 c, e, f -------------------------------------
USE solar_bd;

DROP TRIGGER IF EXISTS delivery_row_limit;
DROP TRIGGER IF EXISTS prevent_delete_electricity_price;
DROP TRIGGER IF EXISTS log_delivery_deletion;

-- e ------------------------------------------------
DELIMITER //

CREATE TRIGGER delivery_row_limit
BEFORE DELETE ON Delivery
FOR EACH ROW
BEGIN
  DECLARE row_count INT;
  SELECT COUNT(*) INTO row_count FROM Delivery;

  IF row_count < 0 OR row_count >= 500 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Row limit violation for Delivery table';
  END IF;
END //

DELIMITER ;

-- ---------------------------------------------------

-- c ---------------------------------------------------
DELIMITER //

CREATE TRIGGER prevent_delete_electricity_price
BEFORE DELETE ON electricity_price
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Deletion not allowed for electricity_price table';
END //

DELIMITER ;

-- f --------------------------------------------------
DELIMITER //

DROP TABLE IF EXISTS deletion_log;

CREATE TABLE IF NOT EXISTS deletion_log (
    `id` INT NOT NULL AUTO_INCREMENT,
    `table_name` VARCHAR(50) NOT NULL,
    `deleted_id` INT NOT NULL,
    `deleted_timestamp` DATETIME NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TRIGGER log_delivery_deletion
AFTER DELETE ON Delivery
FOR EACH ROW
BEGIN
  INSERT INTO deletion_log (table_name, deleted_id, deleted_timestamp)
  VALUES ('Delivery', OLD.id, NOW());
END //

DELIMITER ;
-- ----------------------------------------------