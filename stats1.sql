-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 10:23 AM
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
-- Table structure for table `stats1`
--

CREATE TABLE `stats1` (
  `player` varchar(60) NOT NULL,
  `matches` int(60) NOT NULL,
  `runs` int(60) NOT NULL,
  `100s` int(60) NOT NULL,
  `50s` int(60) NOT NULL,
  `value` int(60) NOT NULL,
  `ctg` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stats1`
--

INSERT INTO `stats1` (`player`, `matches`, `runs`, `100s`, `50s`, `value`, `ctg`) VALUES
('Virat Kohli', 189, 8257, 28, 43, 120, 'BAT'),
('Yuvraj Singh', 86, 3589, 10, 21, 100, 'BAT'),
('A Rahane', 158, 5435, 11, 31, 100, 'BAT'),
('Shikar Dhawan', 25, 565, 2, 1, 8, 'BAT'),
('Mahendra Singh Dhoni', 78, 2573, 3, 19, 75, 'WK'),
('Hardik Pandya', 70, 77, 0, 0, 75, 'AR'),
('Ravindra Jadeja', 16, 1, 0, 0, 85, 'AR'),
('Kedhar Jadhav', 111, 675, 0, 1, 90, 'BAT'),
('R Ashwin', 136, 1914, 0, 10, 100, 'AR'),
('Umesh Yadav', 296, 9496, 10, 64, 110, 'BWL'),
('Jasprit Bumrah', 73, 1365, 0, 8, 60, 'BWL'),
('Bhuvaneshwar Kumar', 17, 289, 0, 2, 75, 'BWL'),
('Rohit Sharma', 304, 8701, 14, 52, 85, 'BAT'),
('Dinesh Kartik', 11, 111, 0, 0, 75, 'WK'),
('Prithvi Shaw', 140, 1356, 30, 40, 50, 'BAT'),
('Mayank Agarwal', 129, 1000, 24, 34, 77, 'BAT'),
('S Iyer', 123, 1132, 12, 36, 116, 'BAT'),
('Manish Pandey', 55, 112, 19, 23, 122, 'BAT'),
('Yuvendra Chahal', 156, 100, 2, 6, 98, 'BWL'),
('Mohammed Shami', 89, 52, 3, 8, 123, 'BWL'),
('Kuldeep Jadhav', 200, 113, 13, 15, 114, 'BWL'),
('KL Rahul', 157, 2189, 45, 56, 2134, 'WK');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
