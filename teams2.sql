-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 10:25 AM
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
-- Table structure for table `teams2`
--

CREATE TABLE `teams2` (
  `no` int(60) NOT NULL,
  `name` varchar(60) NOT NULL,
  `players` varchar(60) NOT NULL,
  `value` int(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teams2`
--

INSERT INTO `teams2` (`no`, `name`, `players`, `value`) VALUES
(1, 'navin', 'Dinesh Kartik', 577),
(2, 'navin', 'R Ashwin', 302),
(3, 'navin', 'Hardik Pandya', 349),
(4, 'navin', 'Umesh Yadav', 570),
(5, 'navin', 'Mohammed Shami', 57),
(6, 'navin', 'Bhuvaneshwar Kumar', 47),
(7, 'navin', 'Jasprit Bumrah', 150),
(8, 'navin', 'Virat Kohli', 477),
(9, 'navin', 'Manish Pandey', 50),
(10, 'navin', 'A Rahane', 132),
(11, 'navin', 'Prithvi Shaw', 47),
(12, 'ipl', 'Mahendra Singh Dhoni', 444),
(13, 'ipl', 'Yuvraj Singh', 453),
(14, 'ipl', 'Hardik Pandya', 45),
(15, 'ipl', 'Umesh Yadav', 54),
(16, 'ipl', 'Kuldeep Jadhav', 57),
(17, 'ipl', 'Mohammed Shami', 150),
(18, 'ipl', 'Jasprit Bumrah', 257),
(19, 'ipl', 'Kedhar Jadhav', 477),
(20, 'ipl', 'Shikar Dhawan', 50),
(21, 'ipl', 'Mayank Agarwal', 236),
(22, 'ipl', 'Rohit Sharma', 208);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `teams2`
--
ALTER TABLE `teams2`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `teams2`
--
ALTER TABLE `teams2`
  MODIFY `no` int(60) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
