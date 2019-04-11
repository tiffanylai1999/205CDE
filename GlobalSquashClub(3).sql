-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 11, 2019 at 10:21 AM
-- Server version: 5.7.25-0ubuntu0.16.04.2
-- PHP Version: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `GlobalSquashClub`
--

-- --------------------------------------------------------

--
-- Table structure for table `c001`
--

CREATE TABLE `c001` (
  `name` varchar(55) NOT NULL,
  `id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `c001`
--

INSERT INTO `c001` (`name`, `id`) VALUES
('haha', 13),
('hayton', 10),
('mky', 8),
('test', 11);

-- --------------------------------------------------------

--
-- Table structure for table `c002`
--

CREATE TABLE `c002` (
  `name` varchar(55) NOT NULL,
  `id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `coaches`
--

CREATE TABLE `coaches` (
  `id` int(12) NOT NULL,
  `name` varchar(55) NOT NULL,
  `phone` int(12) NOT NULL,
  `email` varchar(55) NOT NULL,
  `year_of_teaching` int(2) NOT NULL,
  `coach_level` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `coaches`
--

INSERT INTO `coaches` (`id`, `name`, `phone`, `email`, `year_of_teaching`, `coach_level`) VALUES
(1, 'Anthony So', 96723197, 'assquash@hotmail.com', 30, 2),
(2, 'Helen Cheung', 96723198, 'asohelen@gmail.com', 20, 1),
(3, 'Kevin Chan', 61821865, 'kc_him@yahoo.com.hk', 10, 1),
(4, 'Ida Cheung', 93001615, 'squash1999@hotmail.com.hk', 10, 1),
(5, 'Hayton Ip', 54239802, 'haytoniky@gmail.com', 10, 1),
(9, 'test', 9999999, 'test@gmail.com', 2, 2),
(10, 'stephan', 99999999, '999@gmail.com', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `commentCode` int(2) NOT NULL,
  `commentName` varchar(55) NOT NULL,
  `commentEmail` varchar(55) NOT NULL,
  `commentInfo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`commentCode`, `commentName`, `commentEmail`, `commentInfo`) VALUES
(1, 'haha', 'haha@gmail.com', 'hahaha\r\n'),
(2, 'abc', 'abc@gmail.com', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssssssssssssssssssssssssssdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'),
(3, 'test', 'test@gmail.com', 'testing'),
(4, 'aaa', 'aaa@gmail.com', '1111');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `courseCode` mediumint(9) NOT NULL,
  `date` datetime NOT NULL,
  `avaliable_seats` int(2) NOT NULL,
  `coaches` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`courseCode`, `date`, `avaliable_seats`, `coaches`) VALUES
(1, '2019-04-13 13:00:00', 20, 'Anthony So, Helen Cheung, Ida Cheung'),
(2, '2019-04-07 14:00:00', 20, 'Anthony So, Kelvin Chan, Hayton Ip');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userName` varchar(55) NOT NULL,
  `contactNo` int(12) NOT NULL,
  `userEmail` varchar(55) NOT NULL,
  `password` varchar(8) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `userType` enum('1','2') CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userName`, `contactNo`, `userEmail`, `password`, `dateOfBirth`, `userType`) VALUES
('haha', 99999999, 'haha@gmail.com', '123456', '1898-01-01', '2'),
('Hayton Ip', 99999999, 'Haytoniky@gmail.com', '123456', '1898-01-01', '1'),
('kkk', 99999999, 'kkk@gmail.com', '123456', '1898-01-01', '1'),
('MKY', 99999111, 'mky@gmail.com', '123456', '1898-03-31', '2'),
('stephan', 99999999, '999@gmail.com', '1111111', '2019-04-16', '1'),
('test', 99999999, 'test@gmail.com', '123456', '2018-03-09', '1'),
('testing', 99999991, 'testing@gmail.com', '123456', '2019-04-16', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `c001`
--
ALTER TABLE `c001`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `c002`
--
ALTER TABLE `c002`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `coaches`
--
ALTER TABLE `coaches`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`commentCode`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`courseCode`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userName`,`userEmail`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `c001`
--
ALTER TABLE `c001`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `coaches`
--
ALTER TABLE `coaches`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `commentCode` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `courseCode` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
