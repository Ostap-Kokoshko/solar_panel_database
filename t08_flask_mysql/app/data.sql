SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE DATABASE IF NOT EXISTS solar_bd;
USE solar_bd;

DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS owner;
DROP TABLE IF EXISTS installation_address;
DROP TABLE IF EXISTS solar_system;
DROP TABLE IF EXISTS owner_solar_system;
DROP TABLE IF EXISTS battery;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS electricity_price;
DROP TABLE IF EXISTS energy_sale;
DROP TABLE IF EXISTS solar_panel;
DROP TABLE IF EXISTS solar_system_has_solar_panel;
DROP TABLE IF EXISTS delivery;
DROP TABLE IF EXISTS solar_bd.order;
DROP TABLE IF EXISTS solar_panel_has_battery;
DROP TABLE IF EXISTS order_has_solar_system;


CREATE TABLE region (
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE city (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`, `region_name`),
  INDEX `fk_city_region1_idx` (`region_name` ASC) VISIBLE,
  CONSTRAINT `fk_city_region1`
    FOREIGN KEY (`region_name`)
    REFERENCES `solar_bd`.`region` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE owner (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(13) NOT NULL,
  `city_id` INT NOT NULL,
  `city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE,
  INDEX `fk_owner_city1_idx` (`city_id` ASC, `city_region_name` ASC) VISIBLE,
  CONSTRAINT `fk_owner_city1`
    FOREIGN KEY (`city_id` , `city_region_name`)
    REFERENCES `solar_bd`.`city` (`id` , `region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE installation_address (
  `id` INT NOT NULL AUTO_INCREMENT,
  `street` VARCHAR(45) NOT NULL,
  `postal_index` INT NOT NULL,
  `city_id` INT NOT NULL,
  `city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`, `city_id`, `city_region_name`),
  INDEX `fk_installation_address_city1_idx` (`city_id` ASC, `city_region_name` ASC) VISIBLE,
  CONSTRAINT `fk_installation_address_city1`
    FOREIGN KEY (`city_id` , `city_region_name`)
    REFERENCES `solar_bd`.`city` (`id` , `region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE solar_system (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `battery_capacity` INT NOT NULL,
  `price` DECIMAL NOT NULL,
  `installation_address_id` INT NOT NULL,
  `installation_address_city_id` INT NOT NULL,
  `installation_address_city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`, `installation_address_id`, `installation_address_city_id`, `installation_address_city_region_name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_solar_system_installation_address1_idx` (`installation_address_id` ASC, `installation_address_city_id` ASC, `installation_address_city_region_name` ASC) VISIBLE,
  CONSTRAINT `fk_solar_system_installation_address1`
    FOREIGN KEY (`installation_address_id` , `installation_address_city_id` , `installation_address_city_region_name`)
    REFERENCES `solar_bd`.`installation_address` (`id` , `city_id` , `city_region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE owner_solar_system (
  `owner_id` INT NOT NULL,
  `solar_system_id` INT NOT NULL,
  `system_count` INT NOT NULL,
  `owner_count` INT NOT NULL,
  PRIMARY KEY (`owner_id`, `solar_system_id`),
  INDEX `fk_owner_has_solar_system_solar_system1_idx` (`solar_system_id` ASC) VISIBLE,
  INDEX `fk_owner_has_solar_system_owner_idx` (`owner_id` ASC) VISIBLE,
  CONSTRAINT `fk_owner_has_solar_system_owner`
    FOREIGN KEY (`owner_id`)
    REFERENCES `solar_bd`.`owner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_owner_has_solar_system_solar_system1`
    FOREIGN KEY (`solar_system_id`)
    REFERENCES `solar_bd`.`solar_system` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE battery (
  `capacity` INT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE client (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `phone` DECIMAL NOT NULL,
  `birthday` DATE NULL,
  `email` VARCHAR(45) NULL,
  `gander` VARCHAR(45) NOT NULL,
  `age` INT NULL,
  `city_id` INT NOT NULL,
  `city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,
  INDEX `fk_client_city1_idx` (`city_id` ASC, `city_region_name` ASC) VISIBLE,
  CONSTRAINT `fk_client_city1`
    FOREIGN KEY (`city_id` , `city_region_name`)
    REFERENCES `solar_bd`.`city` (`id` , `region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE electricity_price (
  `id` INT NOT NULL AUTO_INCREMENT,
  `time_date` DATETIME NOT NULL,
  `price` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `time_date_UNIQUE` (`time_date` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE energy_sale (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NULL,
  `electricity_price_id` INT NOT NULL,
  PRIMARY KEY (`id`, `electricity_price_id`),
  INDEX `fk_energy_sale_electricity_price1_idx` (`electricity_price_id` ASC) VISIBLE,
  CONSTRAINT `fk_energy_sale_electricity_price1`
    FOREIGN KEY (`electricity_price_id`)
    REFERENCES `solar_bd`.`electricity_price` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE solar_panel (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NOT NULL,
  `power` INT NOT NULL,
  `is_tilt_angel` TINYINT NOT NULL,
  `tilt_angle` INT NULL,
  `time` TIME NOT NULL,
  `battery_charge` INT NULL,
  `energy_sale_id` INT NOT NULL,
  `energy_sale_electricity_price_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_solar_panel_energy_sale1_idx` (`energy_sale_id` ASC, `energy_sale_electricity_price_id` ASC) VISIBLE,
  CONSTRAINT `fk_solar_panel_energy_sale1`
    FOREIGN KEY (`energy_sale_id` , `energy_sale_electricity_price_id`)
    REFERENCES `solar_bd`.`energy_sale` (`id` , `electricity_price_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE solar_system_has_solar_panel (
  `solar_system_id` INT NOT NULL,
  `solar_panel_id` INT NOT NULL,
  `panel_count` INT NOT NULL,
  PRIMARY KEY (`solar_system_id`, `solar_panel_id`),
  INDEX `fk_solar_system_has_solar_panel_solar_panel1_idx` (`solar_panel_id` ASC) VISIBLE,
  INDEX `fk_solar_system_has_solar_panel_solar_system1_idx` (`solar_system_id` ASC) VISIBLE,
  CONSTRAINT `fk_solar_system_has_solar_panel_solar_system1`
    FOREIGN KEY (`solar_system_id`)
    REFERENCES `solar_bd`.`solar_system` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solar_system_has_solar_panel_solar_panel1`
    FOREIGN KEY (`solar_panel_id`)
    REFERENCES `solar_bd`.`solar_panel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE delivery (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


CREATE TABLE solar_bd.order (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `delivery_id` INT NOT NULL,
  `is_delivery` TINYINT NOT NULL,
  `delivery_time` DATETIME NULL,
  `street_address` VARCHAR(45) NULL,
  `total_price` DECIMAL NOT NULL,
  `city_id` INT NOT NULL,
  `city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_order_client1_idx` (`client_id` ASC) VISIBLE,
  INDEX `fk_order_delivery1_idx` (`delivery_id` ASC) VISIBLE,
  INDEX `fk_order_city1_idx` (`city_id` ASC, `city_region_name` ASC) VISIBLE,
  CONSTRAINT `fk_order_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `solar_bd`.`client` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_delivery1`
    FOREIGN KEY (`delivery_id`)
    REFERENCES `solar_bd`.`delivery` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_city1`
    FOREIGN KEY (`city_id` , `city_region_name`)
    REFERENCES `solar_bd`.`city` (`id` , `region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE solar_panel_has_battery (
  `solar_panel_id` INT NOT NULL,
  `battery_id` INT NOT NULL,
  PRIMARY KEY (`solar_panel_id`, `battery_id`),
  INDEX `fk_solar_panel_has_battery_battery1_idx` (`battery_id` ASC) VISIBLE,
  INDEX `fk_solar_panel_has_battery_solar_panel1_idx` (`solar_panel_id` ASC) VISIBLE,
  CONSTRAINT `fk_solar_panel_has_battery_solar_panel1`
    FOREIGN KEY (`solar_panel_id`)
    REFERENCES `solar_bd`.`solar_panel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solar_panel_has_battery_battery1`
    FOREIGN KEY (`battery_id`)
    REFERENCES `solar_bd`.`battery` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE order_has_solar_system (
  `order_id` INT NOT NULL,
  `solar_system_id` INT NOT NULL,
  `solar_system_installation_address_id` INT NOT NULL,
  `solar_system_installation_address_city_id` INT NOT NULL,
  `solar_system_installation_address_city_region_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`order_id`, `solar_system_id`, `solar_system_installation_address_id`, `solar_system_installation_address_city_id`, `solar_system_installation_address_city_region_name`),
  INDEX `fk_order_has_solar_system_solar_system1_idx` (`solar_system_id` ASC, `solar_system_installation_address_id` ASC, `solar_system_installation_address_city_id` ASC, `solar_system_installation_address_city_region_name` ASC) VISIBLE,
  INDEX `fk_order_has_solar_system_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_solar_system_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `solar_bd`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_solar_system_solar_system1`
    FOREIGN KEY (`solar_system_id` , `solar_system_installation_address_id` , `solar_system_installation_address_city_id` , `solar_system_installation_address_city_region_name`)
    REFERENCES `solar_bd`.`solar_system` (`id` , `installation_address_id` , `installation_address_city_id` , `installation_address_city_region_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


INSERT INTO region (name) VALUES
('Frankivsk'), ('Poltava'), ('Kyiv'), ('Lviv'), ('Odesa'),
('Ternopil'), ('Volyn'), ('region1'), ('region2'), ('region3');


INSERT INTO city (id, name, region_name) VALUES
('1', 'Boryspil', 'Kyiv'), ('2', 'Stryi', 'Lviv'), ('3', 'Berezivka', 'Odesa'),
('4', 'Chortkiv', 'Ternopil'), ('5', 'Lutsk', 'Volyn'), ('6', 'Ivano', 'Frankivsk'), ('7', 'Pol', 'Poltava'),
('8', 'city1', 'region1'), ('9', 'city2', 'region2'), ('10', 'city3', 'region3');


INSERT INTO owner (id, name, email, phone_number, city_id, city_region_name) VALUES
('1', 'LvivBud', 'IFgaohfai@gmail.com', '+62062', '2', 'Lviv'),
('2', 'KyivBud', 'gbip59b@gmail.com', '+2976961', '1', 'Kyiv'),
('3', 'VolynBud', '57golhgiqh@gmail.com', '+38738970', '5', 'Volyn'),
('4', 'TernopilBud', '6723iwbo@gmail.com', '+58927590', '4', 'Ternopil'),
('5', 'OdesaBud', 'ghqihgqo@gmail.com', '+8292127', '3', 'Odesa'),
('6', 'FrankivskBud', 'frank@gmail.com', '+56356893', '6', 'Frankivsk'),
('7', 'PoltavaBud', 'pol@gmail.com', '+1468291', '7', 'Poltava'),
('8', 'owner1', 'owner1@gmail.com', '+72762906', '8', 'region1'),
('9', 'owner2', 'owner2@gmail.com', '+52869120', '9', 'region2'),
('10', 'owner3', 'owner3@gmail.com', '+058095', '10', 'region3');


INSERT INTO installation_address (id, street, postal_index, city_id, city_region_name) VALUES
('1', 'Chornovola', '79100', '1', 'Kyiv'), ('2', 'Frunzivka', '36737', '3', 'Odesa'),
('3', 'Masaryka', '79012', '2', 'Lviv'), ('4', 'Schevchenko', '79390', '5', 'Volyn'),
('5', 'Tern', '52370', '4', 'Ternopil'), ('6', 'Frank', '56295', '6', 'Frankivsk'),
('7', 'Pol', '62767', '7', 'Poltava'), ('8', 'street1', '14747', '8', 'region1'),
('9', 'street2', '57125', '9', 'region2'), ('10', 'street3', '67829', '10', 'region3');


INSERT INTO solar_system (id, name, battery_capacity, price, installation_address_id, installation_address_city_id, installation_address_city_region_name) VALUES
('1', 'Very small system', '250', '10000', '3', '2', 'Lviv'), ('2', 'Small system', '600', '20000', '1', '1', 'Kyiv'),
('3', 'Medium system', '1050', '30000', '4', '5', 'Volyn'), ('4', 'Large system', '1600', '40000', '5', '4', 'Ternopil'),
('5', 'Very Large System', '2250', '50000', '2', '3', 'Odesa'), ('6', 'XXL System', '3000', '55000', '6', '6', 'Frankivsk'),
('7', 'XXXL System', '4000', '60000', '7', '7', 'Poltava'), ('8', 'System1', '5000', '65000', '8', '8', 'region1'),
('9', 'System2', '1900', '45000', '9', '9', 'region2'), ('10', 'System3', '6000', '70000', '10', '10', 'region3');
INSERT INTO owner_solar_system (owner_id, solar_system_id, system_count, owner_count) VALUES
('1', '1', '1', '1'), ('2', '2', '2', '2'), ('3', '3', '3', '3'), ('4', '4', '4', '4'), ('5', '5', '5', '5'),
('6', '6', '6', '6'), ('7', '7', '7', '7'), ('8', '8', '8', '8'), ('9', '9', '9', '9'), ('10', '10', '10', '10');


INSERT INTO battery (capacity, id, name) VALUES
('250', '1', 'VG 12-100 Gel'), ('300', '2', 'ALVA battery AW6-7'), ('350', '3', 'ALVA battery AW12-5'),
('400', '4', 'Altek ABT-7-12-AGM'), ('450', '5', 'Altek ABT-100-12-GEL'), ('500', '6', 'Altek ABT-500-13-GEL'),
('550', '7', 'ALVA battery AW550'), ('600', '8', 'battery1'), ('650', '9', 'battery2'), ('700', '10', 'battery3');


INSERT INTO client (id, name, lastname, phone, birthday, email, gander, age, city_id, city_region_name) VALUES
('1', 'Ostap', 'Kokoshko', '38529357', '2004-10-20', 'ostapk2004@gmail.com', 'Male', '18', '2', 'Lviv'),
('2', 'Yura', 'Dubyk', '385676591', '1986-05-13', 'yura@gmail.com', 'Male', '37', '1', 'Kyiv'),
('3', 'Sasha', 'Syr', '3852372072', '2003-11-11', 'sasha@gmail.com', 'Female', '20', '5', 'Volyn'),
('4', 'Sasha', 'Sen', '3841240', '1993-11-13', 'sen@gmail.com', 'Male', '30', '4', 'Ternopil'),
('5', 'Oleg', 'Ostash', '26865768', '1988-02-21', NULL, 'Female', '35', '3', 'Odesa'),
('6', 'Denis', 'Olinsky', '6262967', '2007-08-31', 'den@gmail.com', 'Male', '16', '6', 'Frankivsk'),
('7', 'Andriy', 'Buznia', '155692', '1999-02-21', NULL, 'Male', '24', '7', 'Poltava'),
('8', 'cl_name1', 'cl_lastname1', '6286891', '1970-03-21', NULL, 'Female', '72', '8', 'region1'),
('9', 'cl_name2', 'cl_lastname2', '616916', '1970-03-21', NULL, 'Male', '34', '9', 'region2'),
('10', 'cl_name3', 'cl_lastname3', '5615691', '1970-03-21', NULL, 'Female', '54', '10', 'region3');


INSERT INTO electricity_price (id, time_date, price) VALUES
('1', '2024-10-12 12:13:14', '100'), ('2', '2023-10-12 12:13:14', '90'), ('3', '2022-10-12 12:13:14', '80'),
('4', '2021-10-12 12:13:14', '70'), ('5', '2020-10-12 12:13:14', '60'), ('6', '2019-10-12 12:13:14', '50'),
('7', '2023-11-01 12:13:14', '110'), ('8', '2023-12-01 12:13:14', '120'), ('9', '2024-12-01 12:13:14', '130'),
('10', '2025-11-01 12:13:14', '110');


INSERT INTO energy_sale (id, quantity, electricity_price_id) VALUES
('1', '200', '1'), ('2', '300', '2'), ('3', NULL, '3'), ('4', '100', '4'), ('5', NULL, '5'),
('6', '50', '6'), ('7', '150', '7'), ('8', NULL, '8'), ('9', '210', '9'), ('10', NULL, '10');


INSERT INTO solar_panel (id, type, power, is_tilt_angel, tilt_angle, time, battery_charge, energy_sale_id, energy_sale_electricity_price_id) VALUES
('1', 'Monocrystalline', '150', '0', NULL, '14:13:12', '20', '1', '1'),
('2', 'Polycrystalline', '200', '1', '30', '12:13:14', '45', '2', '2'),
('3', 'PERC', '250', '0', NULL, '14:13:12', NULL, '3', '3'),
('4', 'Thin-film', '300', '0', NULL, '12:13:14', '30', '4', '4'),
('5', 'PERC', '350', '1', '45', '14:13:12', '100', '5', '5'),
('6', 'Thin-film', '400', '0', '15', '14:13:12', '100', '6', '6'),
('7', 'Monocrystalline', '450', '0', '20', '14:13:12', '50', '7', '7'),
('8', 'Polycrystalline', '325', '1', NULL, '12:13:14', '75', '8', '8'),
('9', 'PERC', '500', '1', '30', '12:13:14', NULL, '9', '9'),
('10', 'Thin-film', '550', '0', '35', '12:13:14', '30', '10', '10');


INSERT INTO solar_system_has_solar_panel (solar_system_id, solar_panel_id, panel_count) VALUES
('1', '1', '1'), ('2', '2', '2'), ('3', '3', '3'), ('4', '4', '4'), ('5', '5', '5'),
('6', '6', '6'), ('7', '7', '7'), ('8', '8', '8'), ('9', '9', '9'), ('10', '10', '10');


INSERT INTO delivery (id, name, price) VALUES
('1', 'Slow', '100'), ('2', 'Normal', '150'), ('3', 'Fast', '200'), ('4', 'Very fast', '250'), ('5', 'Very Slow', '50'),
('6', 'None', '0'), ('7', 'Hasty', '300'), ('8', 'Quick', '225'), ('9', 'Delivery1', '75'), ('10', 'Delivery2', '125');


INSERT INTO solar_bd.order (id, client_id, delivery_id, is_delivery, delivery_time, street_address, total_price, city_id, city_region_name) VALUES
('1', '1', '1', '1', '2023-10-12 12:13:14', 'Masaryka', '1000', '2', 'Lviv'),
('2', '2', '6', '0', NULL, NULL, '1500', '1', 'Kyiv'),
('3', '3', '6', '0', NULL, NULL, '2000', '5', 'Volyn'),
('4', '4', '4', '1', '2023-11-12 09:10:10', 'Vushnivka', '1300', '4', 'Ternopil'),
('5', '5', '6', '0', NULL, NULL, '1400', '3', 'Odesa'),
('6', '6', '7', '1', '2023-10-12 12:13:14', 'Frank', '1700', '6', 'Frankivsk'),
('7', '7', '8', '1', '2023-11-12 12:13:14', 'Pol', '1400', '7', 'Poltava'),
('8', '8', '9', '1', '2023-12-12 12:13:14', 'street1', '1600', '8', 'region1'),
('9', '9', '6', '0', NULL, NULL, '1000', '9', 'region2'),
('10', '10', '6', '0', NULL, NULL, '900', '10', 'region3');


INSERT INTO solar_panel_has_battery (solar_panel_id, battery_id) VALUES
('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10');


INSERT INTO order_has_solar_system (order_id, solar_system_id, solar_system_installation_address_id, solar_system_installation_address_city_id, solar_system_installation_address_city_region_name) VALUES
('1', '1', '3', '2', 'Lviv'), ('2', '2', '1', '1', 'Kyiv'), ('3', '3', '4', '5', 'Volyn'), ('4', '4', '5', '4', 'Ternopil'),
('5', '5', '2', '3', 'Odesa'), ('6', '6', '6', '6', 'Frankivsk'), ('7', '7', '7', '7', 'Poltava'), ('8', '8', '8', '8', 'region1'),
('9', '9', '9', '9', 'region2'), ('10', '10', '10', '10', 'region3');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
