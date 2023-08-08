-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 伺服器版本:                        11.2.0-MariaDB - mariadb.org binary distribution
-- 伺服器作業系統:                      Win64
-- HeidiSQL 版本:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 傾印 std_rule 的資料庫結構
CREATE DATABASE IF NOT EXISTS `std_rule` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `std_rule`;

-- 傾印  資料表 std_rule.backplane_parts 結構
CREATE TABLE IF NOT EXISTS `backplane_parts` (
  `item_no` varchar(20) NOT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`)),
  `factory` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.backplane_parts 的資料：~5 rows (近似值)
REPLACE INTO `backplane_parts` (`item_no`, `parts`, `factory`) VALUES
	('58-99532-0000', '[["PCIex16","1"],["PCI","1"]]', 'TPMC'),
	('58-99533-0000', '[["PCIex16","1"],["PCIex4","2"],["PCI","1"]]', 'TPMC'),
	('59-46930-1000', '[["PCIex16","1"],["PCI","1"]]', 'SHMC'),
	('59-46931-0000', '[["PCIex16","1"],["PCIex4","2"],["PCI","1"]]', 'SHMC'),
	('59-46932-0000', '[["PCIex16","1"],["PCIex4","1"]]', 'SHMC');

-- 傾印  資料表 std_rule.cpu 結構
CREATE TABLE IF NOT EXISTS `cpu` (
  `item_no` varchar(20) NOT NULL,
  `token` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.cpu 的資料：~6 rows (近似值)
REPLACE INTO `cpu` (`item_no`, `token`, `name`) VALUES
	('01-I7180-0060', '1', 'i7-9700TE'),
	('01-I7220-0030', '2', 'i5-9500TE'),
	('01-I7220-0040', '3', 'i3-9100TE'),
	('01-I7260-0020', 'A', 'i7-9700E'),
	('01-I7290-0030', '4', 'Celeron G4900T'),
	('01-I8330-0020', 'X', 'Xeon E-2278GE');

-- 傾印  資料表 std_rule.description_to_motherboard 結構
CREATE TABLE IF NOT EXISTS `description_to_motherboard` (
  `item_no` varchar(20) NOT NULL,
  `description` varchar(20) DEFAULT NULL,
  `factory` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.description_to_motherboard 的資料：~11 rows (近似值)
REPLACE INTO `description_to_motherboard` (`item_no`, `description`, `factory`) VALUES
	('58-99480-0000', '51', 'TPMC'),
	('58-99529-0000', '61', 'TPMC'),
	('58-99529-1000', '61', 'TPMC'),
	('58-99529-2000', '51', 'TPMC'),
	('59-44833-0000', '61', 'SHMC'),
	('59-44833-1000', '61', 'SHMC'),
	('59-44833-2000', '51', 'SHMC'),
	('59-44833-3000', '51MXM', 'SHMC'),
	('59-44833-4000', '61MXM', 'SHMC'),
	('59-44833-7000', '51', 'SHMC'),
	('59-44833-7100', '51', 'SHMC');

-- 傾印  資料表 std_rule.item_type 結構
CREATE TABLE IF NOT EXISTS `item_type` (
  `item_no` varchar(20) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.item_type 的資料：~60 rows (近似值)
REPLACE INTO `item_type` (`item_no`, `type`) VALUES
	('01-I7180-0060', 'CPU'),
	('01-I7220-0030', 'CPU'),
	('01-I7220-0040', 'CPU'),
	('01-I7260-0020', 'CPU'),
	('01-I7290-0030', 'CPU'),
	('01-I8330-0020', 'CPU'),
	('29-6B400-L4A0', 'Memory'),
	('29-6B800-L430', 'Memory'),
	('29-6B800-L480', 'Memory'),
	('29-6BC00-L430', 'Memory'),
	('29-6BC00-L480', 'Memory'),
	('32-20639-0000-A0', 'Cooler'),
	('32-20640-0000-A0', 'Cooler'),
	('32-20641-0000-A0', 'Cooler'),
	('32-20642-0000-A0', 'Cooler'),
	('32-20797-0200-A0', 'Cooler'),
	('32-20830-0200-A0', 'Cooler'),
	('32-20905-0000-A0', 'Cooler'),
	('32-20912-0000-A0', 'Cooler'),
	('32-20914-0000-A0', 'Cooler'),
	('51-49069-0A10-A0', 'FPC'),
	('55-46933-0000', 'Transfer'),
	('55-49065-0000', 'FPC'),
	('57-60017-1000-A0', 'Chassis'),
	('57-60018-1000-A0', 'Chassis'),
	('57-60019-1000-A0', 'Chassis'),
	('57-60020-1000-A0', 'Chassis'),
	('58-04019-1000-A0', 'ASSM_Part'),
	('58-04020-1000-A0', 'ASSM_Part'),
	('58-04021-1000-A0', 'ASSM_Part'),
	('58-04022-1000-A0', 'ASSM_Part'),
	('58-04028-1000-A0', 'ASSM_Part'),
	('58-04029-1000-A0', 'ASSM_Part'),
	('58-04030-1000-A0', 'ASSM_Part'),
	('58-04031-0000-A0', 'ASSM_Part'),
	('58-04032-1000-A0', 'ASSM_Part'),
	('58-06209-0000-A0', 'Thermal_Parts'),
	('58-06220-0000-A0', 'Thermal_Parts'),
	('58-10087-0000', 'Packing_Box'),
	('58-10088-0000', 'Packing_Box'),
	('58-10376-0000', 'ASSM_Part'),
	('58-10377-0000', 'ASSM_Part'),
	('58-99480-0000', 'Motherboard'),
	('58-99529-0000', 'Motherboard'),
	('58-99529-1000', 'Motherboard'),
	('58-99529-2000', 'Motherboard'),
	('58-99532-0000', 'BackPlane'),
	('58-99533-0000', 'BackPlane'),
	('59-44833-0000', 'Motherboard'),
	('59-44833-1000', 'Motherboard'),
	('59-44833-2000', 'Motherboard'),
	('59-44833-3000', 'Motherboard'),
	('59-44833-4000', 'Motherboard'),
	('59-44833-7000', 'Motherboard'),
	('59-44833-7100', 'Motherboard'),
	('59-46930-1000', 'BackPlane'),
	('59-46931-0000', 'BackPlane'),
	('59-46932-0000', 'BackPlane'),
	('59-49066-0000', 'FM_Board'),
	('59-49066-1000', 'FM_Board');

-- 傾印  資料表 std_rule.motherboard_parts 結構
CREATE TABLE IF NOT EXISTS `motherboard_parts` (
  `item_no` varchar(20) NOT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`)),
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.motherboard_parts 的資料：~11 rows (近似值)
REPLACE INTO `motherboard_parts` (`item_no`, `parts`) VALUES
	('58-99480-0000', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('58-99529-0000', '[["H310","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('58-99529-1000', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('58-99529-2000', '[["H310","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('59-44833-0000', '[["H310","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('59-44833-1000', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('59-44833-2000', '[["H310","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('59-44833-3000', '[["H310","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","3"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"]]'),
	('59-44833-4000', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","3"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"]]'),
	('59-44833-7000', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","4"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]'),
	('59-44833-7100', '[["C246","1"], ["DP","2"], ["DVI","1"], ["VGA","1"], ["GbE","3"], ["COM","6"], ["USB2","3"], ["USB3","3"], ["USB dongle","1"], ["mPCIe","1"], ["M.2","1"], ["USIM","2"],["audio","1"],["CFast","1"]]');

-- 傾印  資料表 std_rule.must_have 結構
CREATE TABLE IF NOT EXISTS `must_have` (
  `factory` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `description` varchar(20) DEFAULT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.must_have 的資料：~16 rows (近似值)
REPLACE INTO `must_have` (`factory`, `type`, `description`, `parts`) VALUES
	('SHMC', '0', '51', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12510-0010-A0","47-30138-0000-B0"]'),
	('SHMC', '1', '51', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12510-0010-A0","47-30138-0000-B0"]'),
	('TPMC', '0', '51', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12510-1010-A0","47-30138-0000-A0"]'),
	('TPMC', '1', '51', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12510-1010-A0","47-30138-0000-A0"]'),
	('SHMC', '0', '61', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12511-0000-A0","47-30138-0000-B0"]'),
	('SHMC', '1', '61', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12511-0000-A0","47-30138-0000-B0"]'),
	('TPMC', '0', '61', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12511-1000-A0","47-30138-0000-A0"]'),
	('TPMC', '1', '61', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12511-1000-A0","47-30138-0000-A0"]'),
	('SHMC', '0', '51MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12510-2000-A0"]'),
	('SHMC', '1', '51MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12510-2000-A0"]'),
	('TPMC', '0', '51MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12510-1010-A0"]'),
	('TPMC', '1', '51MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12510-1010-A0"]'),
	('SHMC', '0', '61MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12511-2000-A0"]'),
	('SHMC', '1', '61MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12511-2000-A0"]'),
	('TPMC', '0', '61MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","50-40325-3000","47-12511-1000-A0"]'),
	('TPMC', '1', '61MXM', '["20-C2K0C-0000","47-00089-0000","47-12280-0000","47-90004-0010","47-12511-1000-A0"]');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
