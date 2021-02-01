-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 10:22 AM
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
-- Table structure for table `match2`
--

CREATE TABLE `match2` (
  `player` varchar(60) NOT NULL,
  `scored` int(60) NOT NULL,
  `faced` int(60) NOT NULL,
  `fours` int(60) NOT NULL,
  `sixes` int(60) NOT NULL,
  `bowled` int(60) NOT NULL,
  `maiden` int(60) NOT NULL,
  `given` int(60) NOT NULL,
  `wkts` int(60) NOT NULL,
  `catches` int(60) NOT NULL,
  `stumping` int(60) NOT NULL,
  `RO` int(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `match2`
--

INSERT INTO `match2` (`player`, `scored`, `faced`, `fours`, `sixes`, `bowled`, `maiden`, `given`, `wkts`, `catches`, `stumping`, `RO`) VALUES
('Virat Kohli', 102, 98, 8, 2, 0, 0, 0, 0, 0, 0, 1),
('Yuvraj Singh', 12, 20, 1, 0, 48, 0, 36, 1, 0, 0, 0),
('A Rahane', 49, 75, 3, 0, 0, 0, 0, 0, 1, 0, 0),
('Shikar Dhawan', 32, 35, 4, 0, 0, 0, 0, 0, 0, 0, 0),
('Mahendra Singh Dhoni', 56, 45, 3, 1, 0, 0, 0, 0, 3, 2, 0),
('Hardik Pandya', 42, 36, 3, 3, 30, 0, 25, 0, 1, 0, 0),
('Ravindra Jadeja', 18, 10, 1, 1, 60, 3, 50, 2, 1, 0, 1),
('Kedhar Jadhav', 65, 60, 7, 0, 24, 0, 24, 0, 0, 0, 0),
('R Ashwin', 23, 42, 3, 0, 60, 2, 45, 6, 0, 0, 0),
('Umesh Yadav', 0, 0, 0, 0, 54, 0, 50, 4, 1, 0, 0),
('Jasprit Bumrah', 0, 0, 0, 0, 60, 2, 49, 1, 0, 0, 0),
('Bhuvaneshwar Kumar', 15, 12, 2, 0, 60, 1, 46, 2, 0, 0, 0),
('Rohit Sharma', 46, 65, 5, 1, 0, 0, 0, 0, 1, 0, 0),
('Dinesh Kartik', 29, 42, 3, 0, 0, 0, 0, 0, 2, 0, 1),
('Prithvi Shaw', 101, 40, 3, 2, 0, 0, 0, 0, 1, 0, 1),
('Mayank Agarwal', 48, 4, 3, 1, 0, 0, 0, 0, 0, 0, 1),
('S Iyer', 67, 34, 2, 3, 0, 0, 0, 0, 0, 0, 0),
('Manish Pandey', 80, 70, 2, 1, 0, 0, 0, 0, 0, 0, 0),
('Yuvendra Chahal', 30, 20, 0, 0, 40, 2, 37, 5, 2, 0, 0),
('Mohammed Shami', 25, 10, 1, 0, 46, 0, 56, 4, 2, 0, 0),
('Kuldeep Jadhav', 40, 27, 2, 0, 39, 0, 0, 2, 1, 0, 0),
('KL Rahul', 110, 90, 3, 2, 0, 0, 0, 0, 1, 5, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
