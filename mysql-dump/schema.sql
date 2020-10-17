
CREATE SCHEMA IF NOT EXISTS `Smarttbot` ;
USE `Smarttbot` ;

-- -----------------------------------------------------
-- Table `Smarttbot`.`candles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Smarttbot`.`candles` (
  `Moeda` VARCHAR(20) NOT NULL,
  `Periodicidade` INT(11) NOT NULL,
  `Datetime` DATETIME NULL DEFAULT NULL,
  `Open` FLOAT NULL DEFAULT NULL,
  `Low` FLOAT NULL DEFAULT NULL,
  `High` VARCHAR(45) NULL DEFAULT NULL,
  `Close` FLOAT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_bin;

