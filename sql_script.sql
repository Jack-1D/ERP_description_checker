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

-- 傾印  資料表 std_rule.assm_part 結構
CREATE TABLE IF NOT EXISTS `assm_part` (
  `item_no` varchar(20) NOT NULL,
  `graphiccard` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`graphiccard`)),
  `description` varchar(20) DEFAULT NULL,
  `slots` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.assm_part 的資料：~8 rows (近似值)
REPLACE INTO `assm_part` (`item_no`, `graphiccard`, `description`, `slots`) VALUES
	('58-04019-1000-A0', '[]', '51', 0),
	('58-04020-1000-A0', '[]', '61', 2),
	('58-04021-1000-A0', '[]', '61', 4),
	('58-04022-1000-A0', '["P1000","P2000","T1000","RTX3000"]', '51MXM', 0),
	('58-04029-1000-A0', '["P1000","P2000","T1000"]', '61MXM', 2),
	('58-04030-1000-A0', '["P1000","P2000","T1000"]', '61MXM', 4),
	('58-10376-0000', '["RTX3000"]', '61MXM', 2),
	('58-10377-0000', '["RTX3000"]', '61MXM', 4);

-- 傾印  資料表 std_rule.backplane_cooler 結構
CREATE TABLE IF NOT EXISTS `backplane_cooler` (
  `item_no` varchar(20) NOT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`)),
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.backplane_cooler 的資料：~2 rows (近似值)
REPLACE INTO `backplane_cooler` (`item_no`, `parts`) VALUES
	('59-46931-0000', '["32-90292-0000-A0","2"]'),
	('59-46932-0000', '["32-90292-0000-A0","1"]');

-- 傾印  資料表 std_rule.backplane_parts 結構
CREATE TABLE IF NOT EXISTS `backplane_parts` (
  `item_no` varchar(20) NOT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`)),
  `factory` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.backplane_parts 的資料：~6 rows (近似值)
REPLACE INTO `backplane_parts` (`item_no`, `parts`, `factory`) VALUES
	('58-99530-0000', '[["PCIex16","1"],["PCIex4","1"]]', 'SHMC'),
	('58-99532-0000', '[["PCIex16","1"],["PCI","1"]]', 'TPMC'),
	('58-99533-0000', '[["PCIex16","1"],["PCIex4","2"],["PCI","1"]]', 'TPMC'),
	('59-46930-1000', '[["PCIex16","1"],["PCI","1"]]', 'SHMC'),
	('59-46931-0000', '[["PCIex16","1"],["PCIex4","2"],["PCI","1"]]', 'SHMC'),
	('59-46932-0000', '[["PCIex16","1"],["PCIex4","1"]]', 'SHMC');

-- 傾印  資料表 std_rule.cable 結構
CREATE TABLE IF NOT EXISTS `cable` (
  `item_no` varchar(20) NOT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.cable 的資料：~2 rows (近似值)
REPLACE INTO `cable` (`item_no`) VALUES
	('30-21534-0010-A0'),
	('30-21535-0010-A0');

-- 傾印  資料表 std_rule.chassis 結構
CREATE TABLE IF NOT EXISTS `chassis` (
  `item_no` varchar(20) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`description`)),
  `slots` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.chassis 的資料：~4 rows (近似值)
REPLACE INTO `chassis` (`item_no`, `description`, `slots`) VALUES
	('57-60017-1000-A0', '["51"]', 0),
	('57-60018-1000-A0', '["61","61MXM"]', 2),
	('57-60019-1000-A0', '["61","61MXM"]', 4),
	('57-60020-1000-A0', '["51MXM"]', 0);

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

-- 傾印  資料表 std_rule.fpc 結構
CREATE TABLE IF NOT EXISTS `fpc` (
  `item_no` varchar(20) NOT NULL,
  `description` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.fpc 的資料：~2 rows (近似值)
REPLACE INTO `fpc` (`item_no`, `description`) VALUES
	('51-49069-0A10-A0', '61MXM'),
	('55-49065-0000', '51MXM');

-- 傾印  資料表 std_rule.graphiccard_cooler 結構
CREATE TABLE IF NOT EXISTS `graphiccard_cooler` (
  `description` varchar(20) DEFAULT NULL,
  `graphiccard` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `parts` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parts`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.graphiccard_cooler 的資料：~8 rows (近似值)
REPLACE INTO `graphiccard_cooler` (`description`, `graphiccard`, `parts`) VALUES
	('51MXM', 'P1000', '["32-20639-0000-A0"]'),
	('51MXM', 'P2000', '["32-20639-0000-A0"]'),
	('51MXM', 'RTX3000', '["32-20912-0000-A0","32-50032-1000-A0"]'),
	('51MXM', 'T1000', '["32-20905-0000-A0","32-50032-1000-A0"]'),
	('61MXM', 'P2000', '["32-20797-0200-A0"]'),
	('61MXM', 'P1000', '["32-20797-0200-A0"]'),
	('61MXM', 'RTX3000', '["32-20914-0000-A0","32-50032-1000-A0"]'),
	('61MXM', 'T1000', '["32-20830-0200-A0"]');

-- 傾印  資料表 std_rule.item_type 結構
CREATE TABLE IF NOT EXISTS `item_type` (
  `item_no` varchar(20) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.item_type 的資料：~62 rows (近似值)
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
	('30-21534-0010-A0', 'Cable'),
	('30-21535-0010-A0', 'Cable'),
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

-- 傾印  資料表 std_rule.memory 結構
CREATE TABLE IF NOT EXISTS `memory` (
  `item_no` varchar(20) NOT NULL,
  `series` varchar(20) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  `ECC` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.memory 的資料：~5 rows (近似值)
REPLACE INTO `memory` (`item_no`, `series`, `frequency`, `capacity`, `ECC`) VALUES
	('29-6B400-L430', 'DDR4', 2400, 4, 'Non-ECC'),
	('29-6B800-L430', 'DDR4', 2400, 8, 'Non-ECC'),
	('29-6B800-L480', 'DDR4', 2400, 8, 'Non-ECC'),
	('29-6BC00-L430', 'DDR4', 2400, 16, 'Non-ECC'),
	('29-6BC00-L480', 'DDR4', 2400, 16, 'ECC');

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
	('SHMC', '0', '51', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12510-0010-A0","1"],["47-30138-0000-B0","1"]]'),
	('SHMC', '1', '51', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12510-0010-A0","1"],["47-30138-0000-B0","1"]]'),
	('TPMC', '0', '51', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12510-1010-A0","1"],["47-30138-0000-A0","1"]]'),
	('TPMC', '1', '51', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12510-1010-A0","1"],["47-30138-0000-A0","1"]]'),
	('SHMC', '0', '61', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12511-0000-A0","1"],["47-30138-0000-B0","1"]]'),
	('SHMC', '1', '61', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12511-0000-A0","1"],["47-30138-0000-B0","1"]]'),
	('TPMC', '0', '61', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12511-1000-A0","1"],["47-30138-0000-A0","1"]]'),
	('TPMC', '1', '61', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12511-1000-A0","1"],["47-30138-0000-A0","1"]]'),
	('SHMC', '0', '51MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12510-2000-A0","1"]]'),
	('SHMC', '1', '51MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12510-2000-A0","1"]]'),
	('TPMC', '0', '51MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12510-1010-A0","1"]]'),
	('TPMC', '1', '51MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12510-1010-A0","1"]]'),
	('SHMC', '0', '61MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12511-2000-A0","1"]]'),
	('SHMC', '1', '61MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12511-2000-A0","1"]]'),
	('TPMC', '0', '61MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["50-40325-3000","1"],["47-12511-1000-A0","1"]]'),
	('TPMC', '1', '61MXM', '[["20-C2K0C-0000","1"],["47-00089-0000","3"],["47-12280-0000","1"],["47-90004-0010","1"],["47-12511-1000-A0","1"]]');

-- 傾印  資料表 std_rule.packing_box 結構
CREATE TABLE IF NOT EXISTS `packing_box` (
  `item_no` varchar(20) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`description`)),
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.packing_box 的資料：~2 rows (近似值)
REPLACE INTO `packing_box` (`item_no`, `description`) VALUES
	('58-10087-0000', '["51"]'),
	('58-10088-0000', '["61","51MXM","61MXM"]');

-- 傾印  資料表 std_rule.storage 結構
CREATE TABLE IF NOT EXISTS `storage` (
  `item_no` varchar(20) NOT NULL,
  `capacity` int(11) DEFAULT NULL,
  `size` float DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.storage 的資料：~20 rows (近似值)
REPLACE INTO `storage` (`item_no`, `capacity`, `size`) VALUES
	('95-31400-4400', 128, 2280),
	('95-31400-4500', 128, 2280),
	('95-31400-5400', 256, 2280),
	('95-31400-5500', 256, 2280),
	('95-31400-6400', 512, 2280),
	('95-31400-6500', 512, 2280),
	('95-31400-7400', 1000, 2280),
	('95-31400-7500', 1000, 2280),
	('95-31400-8400', 2000, 2280),
	('95-31400-8500', 2000, 2280),
	('95-32400-4100', 128, 2.5),
	('95-32400-4500', 128, 2.5),
	('95-32400-5100', 256, 2.5),
	('95-32400-5500', 256, 2.5),
	('95-32400-6100', 512, 2.5),
	('95-32400-6500', 512, 2.5),
	('95-32400-7100', 1000, 2.5),
	('95-32400-7500', 1000, 2.5),
	('95-32400-8100', 2000, 2.5),
	('95-32400-8500', 2000, 2.5);

-- 傾印  資料表 std_rule.thermal_parts 結構
CREATE TABLE IF NOT EXISTS `thermal_parts` (
  `item_no` varchar(20) NOT NULL,
  `memory_pcs` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  std_rule.thermal_parts 的資料：~2 rows (近似值)
REPLACE INTO `thermal_parts` (`item_no`, `memory_pcs`) VALUES
	('58-06209-0000-A0', 1),
	('58-06220-0000-A0', 2);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
