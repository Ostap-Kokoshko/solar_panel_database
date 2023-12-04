-- 2 a -------------------------------------------
USE solar_bd;

DROP PROCEDURE IF EXISTS insert_into_delivery;

DELIMITER //
CREATE PROCEDURE insert_into_delivery (
	IN delivery_name VARCHAR(45),
    IN delivery_price INT
)
BEGIN
	INSERT INTO `solar_bd`.`delivery` (`name`, `price`)
    VALUES (delivery_name, delivery_price);
END //
DELIMITER ;
-- ----------------------------------------------------

-- 2 b --------------------------------------------------

DROP PROCEDURE IF EXISTS insert_into_owner_has_solar_system;

DELIMITER //
CREATE PROCEDURE insert_into_owner_has_solar_system (
	IN solar_system_id INT,
    IN owner_name VARCHAR(45),
    IN owner_email VARCHAR(45),
    IN owner_phone_number VARCHAR(13),
    IN owner_city_id INT,
    IN owner_region_name VARCHAR(50),
    IN owner_count INT,
    IN solar_system_count INT
)
BEGIN
	DECLARE owner_id INT;

    SELECT id INTO owner_id
    FROM `solar_bd`.`owner`
    WHERE `name` = owner_name AND
    `email` = owner_email AND
    `phone_number` = owner_phone_number AND
    `city_id` = owner_city_id AND
    `city_region_name` = owner_region_name;

    IF owner_id IS NOT NULL THEN
        INSERT INTO `solar_bd`.`owner_solar_system` (`owner_id`, `solar_system_id`, `owner_count`, `system_count`)
        VALUES (owner_id, solar_system_id, owner_count, solar_system_count);
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Owner not found for the given information';
    END IF;
END //
DELIMITER ;
-- ---------------------------------------------

-- 2 c -------------------------------------------

DROP PROCEDURE IF EXISTS insert_ten_into_delivery;

DELIMITER //

CREATE PROCEDURE insert_ten_into_delivery()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 10 DO
        INSERT INTO `solar_bd`.`delivery` (name, price) VALUES (CONCAT('Noname', i), RAND() * 100);
        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;
-- ----------------------------------------------

-- 2 d ------------------------------------------

DROP FUNCTION IF EXISTS get_delivery_stats;
DROP PROCEDURE IF EXISTS get_delivery_statistics;

DELIMITER //

CREATE FUNCTION get_delivery_stats(stat_type VARCHAR(10))
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE result INT;

  IF stat_type = 'Max' THEN
    SELECT MAX(price) INTO result FROM delivery;
  ELSEIF stat_type = 'Min' THEN
    SELECT MIN(price) INTO result FROM delivery;
  ELSEIF stat_type = 'Sum' THEN
    SELECT SUM(price) INTO result FROM delivery;
  ELSEIF stat_type = 'Avg' THEN
    SELECT AVG(price) INTO result FROM delivery;
  ELSE
    SET result = NULL;
  END IF;

  RETURN result;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE get_delivery_statistics(IN stat_type VARCHAR(10))
BEGIN
  DECLARE result INT;

  SET result = get_delivery_stats(stat_type);

  IF result IS NOT NULL THEN
    SELECT CONCAT('The ', stat_type, ' price in delivery is: ', result) AS Result;
  ELSE
    SELECT 'Invalid statistic type' AS Result;
  END IF;
END //

DELIMITER ;
-- --------------------------------------------------

-- 2 e ----------------------------------------------
