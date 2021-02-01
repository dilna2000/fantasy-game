-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2020 at 10:24 AM
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
-- Table structure for table `team`
--

CREATE TABLE `team` (
  `teamno` int(20) NOT NULL,
  `teamname` varchar(20) NOT NULL,
  `playername` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `team`
--

INSERT INTO `team` (`teamno`, `teamname`, `playername`) VALUES
(1, 'SHAL', ''),
(2, 'aefhja', ' '),
(3, '', ' '),
(4, 'shallll', ' '),
(5, 'efguwr', ' '),
(6, 'safsyu', ' '),
(7, 'geth', ' '),
(12, 'teammmmss', 'KL Rahul'),
(13, 'teammmmss', 'Ravindra Jadeja'),
(14, 'teammmmss', 'R Ashwin'),
(15, 'teammmmss', 'Kuldeep Jadhav'),
(16, 'teammmmss', 'Umesh Yadav'),
(17, 'teammmmss', 'Mohammed Shami'),
(18, 'teammmmss', 'Bhuvaneshwar Kumar'),
(19, 'teammmmss', 'A Rahane'),
(20, 'teammmmss', 'Mayank Agarwal'),
(21, 'teammmmss', 'Rohit Sharma'),
(22, 'teammmmss', 'Virat Kohli'),
(23, 'dilnaa', 'Dinesh Kartik'),
(24, 'dilnaa', 'R Ashwin'),
(25, 'dilnaa', 'Hardik Pandya'),
(26, 'dilnaa', 'Umesh Yadav'),
(27, 'dilnaa', 'Jasprit Bumrah'),
(28, 'dilnaa', 'Mohammed Shami'),
(29, 'dilnaa', 'Bhuvaneshwar Kumar'),
(30, 'dilnaa', 'Kedhar Jadhav'),
(31, 'dilnaa', 'Mayank Agarwal'),
(32, 'dilnaa', 'Prithvi Shaw'),
(33, 'dilnaa', 'Rohit Sharma'),
(34, 'reall', 'Mahendra Singh Dhoni'),
(35, 'reall', 'Yuvraj Singh'),
(36, 'reall', 'Ravindra Jadeja'),
(37, 'reall', 'Jasprit Bumrah'),
(38, 'reall', 'Umesh Yadav'),
(39, 'reall', 'Mohammed Shami'),
(40, 'reall', 'Yuvendra Chahal'),
(41, 'reall', 'Mayank Agarwal'),
(42, 'reall', 'A Rahane'),
(43, 'reall', 'Virat Kohli'),
(44, 'reall', 'Prithvi Shaw'),
(45, '', 'KL Rahul'),
(46, '', 'Ravindra Jadeja'),
(47, '', 'R Ashwin'),
(48, '', 'Umesh Yadav'),
(49, '', 'Jasprit Bumrah'),
(50, '', 'Mohammed Shami'),
(51, '', 'Bhuvaneshwar Kumar'),
(52, '', 'Manish Pandey'),
(53, '', 'A Rahane'),
(54, '', 'S Iyer'),
(55, '', 'Virat Kohli'),
(56, 'ipl', 'Mahendra Singh Dhoni'),
(57, 'ipl', 'Yuvraj Singh'),
(58, 'ipl', 'Hardik Pandya'),
(59, 'ipl', 'Umesh Yadav'),
(60, 'ipl', 'Kuldeep Jadhav'),
(61, 'ipl', 'Mohammed Shami'),
(62, 'ipl', 'Jasprit Bumrah'),
(63, 'ipl', 'Kedhar Jadhav'),
(64, 'ipl', 'Shikar Dhawan'),
(65, 'ipl', 'Mayank Agarwal'),
(66, 'ipl', 'Rohit Sharma'),
(67, 'iplteam', 'KL Rahul'),
(68, 'iplteam', 'R Ashwin'),
(69, 'iplteam', 'Hardik Pandya'),
(70, 'iplteam', 'Bhuvaneshwar Kumar'),
(71, 'iplteam', 'Kuldeep Jadhav'),
(72, 'iplteam', 'Mohammed Shami'),
(73, 'iplteam', 'Yuvendra Chahal'),
(74, 'iplteam', 'Prithvi Shaw'),
(75, 'iplteam', 'A Rahane'),
(76, 'iplteam', 'Mayank Agarwal'),
(77, 'iplteam', 'Virat Kohli'),
(78, 'navin', 'Dinesh Kartik'),
(79, 'navin', 'R Ashwin'),
(80, 'navin', 'Hardik Pandya'),
(81, 'navin', 'Umesh Yadav'),
(82, 'navin', 'Mohammed Shami'),
(83, 'navin', 'Bhuvaneshwar Kumar'),
(84, 'navin', 'Jasprit Bumrah'),
(85, 'navin', 'Virat Kohli'),
(86, 'navin', 'Manish Pandey'),
(87, 'navin', 'A Rahane'),
(88, 'navin', 'Prithvi Shaw'),
(89, '', 'KL Rahul'),
(90, '', 'R Ashwin'),
(91, '', 'Ravindra Jadeja'),
(92, '', 'Kuldeep Jadhav'),
(93, '', 'Mohammed Shami'),
(94, '', 'Yuvendra Chahal'),
(95, '', 'Bhuvaneshwar Kumar'),
(96, '', 'A Rahane'),
(97, '', 'Virat Kohli'),
(98, '', 'Mayank Agarwal'),
(99, '', 'Prithvi Shaw'),
(100, 'dfghj', 'KL Rahul'),
(101, 'dfghj', 'R Ashwin'),
(102, 'dfghj', 'Ravindra Jadeja'),
(103, 'dfghj', 'Kuldeep Jadhav'),
(104, 'dfghj', 'Mohammed Shami'),
(105, 'dfghj', 'Yuvendra Chahal'),
(106, 'dfghj', 'Bhuvaneshwar Kumar'),
(107, 'dfghj', 'A Rahane'),
(108, 'dfghj', 'Virat Kohli'),
(109, 'dfghj', 'Mayank Agarwal'),
(110, 'dfghj', 'Prithvi Shaw'),
(111, 'chennai kings', 'KL Rahul'),
(112, 'chennai kings', 'Ravindra Jadeja'),
(113, 'chennai kings', 'R Ashwin'),
(114, 'chennai kings', 'Yuvendra Chahal'),
(115, 'chennai kings', 'Kuldeep Jadhav'),
(116, 'chennai kings', 'Jasprit Bumrah'),
(117, 'chennai kings', 'Bhuvaneshwar Kumar'),
(118, 'chennai kings', 'Mayank Agarwal'),
(119, 'chennai kings', 'Virat Kohli'),
(120, 'chennai kings', 'S Iyer'),
(121, 'chennai kings', 'Kedhar Jadhav');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`teamno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `team`
--
ALTER TABLE `team`
  MODIFY `teamno` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
