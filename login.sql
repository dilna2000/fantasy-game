-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 10:14 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fantasy`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `no` int(10) NOT NULL,
  `name` varchar(60) NOT NULL,
  `number` int(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`no`, `name`, `number`) VALUES
(1, 'bfger', 2147483647),
(2, 'jvhgwr', 2147483647),
(3, 'ejhtuwi4ytu2', 1231231234),
(4, 'fwe', 1234561235),
(5, 'gwr', 2147483647),
(6, 'hfgyt', 2147483647),
(7, 'nbgwhr', 2147483647),
(8, 'qeg2w', 1235421242),
(9, 'bvgh', 2147483647),
(10, 'ng', 2147483647),
(11, 'maeg', 1231231234),
(12, 'DQHEG', 1234563452),
(13, 'nsf', 1232341234),
(14, 'bdh', 2147483647),
(15, 'DILNA', 1231231234),
(16, 'navin bhai', 1234567890),
(17, 'nsbfjd', 1234567897),
(18, 'dsgs', 2147483647),
(19, 'dilna', 2147483647),
(20, 'vgjdaghfgw', 2147483647),
(21, 'feh', 2147483647),
(22, 'vsghaf', 1231231231),
(23, 'ef', 1232343452),
(24, 'svafa', 2147483647),
(25, 'efh', 1231231234),
(26, 'DILNA', 1235673457),
(27, 'DILNA', 1234566537),
(28, 'DILNA', 2147483647),
(29, 'DILNA', 2147483647),
(30, 'XG', 1232343456),
(31, 'sdhg', 2147483647),
(32, 'dafd1', 1231231234),
(33, 'dilna', 2147483647),
(34, 'wt', 2147483647),
(35, 'dnf', 2147483647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
