CREATE TABLE `matchdetails` (
  `MatchID` varchar(45) NOT NULL,
  `Division` varchar(10) NOT NULL,
  `Season` varchar(4) NOT NULL,
  `MatchNo` int(11) NOT NULL,
  `MatchDate` date NOT NULL,
  `HomeTeam` varchar(45) NOT NULL,
  `AwayTeam` varchar(45) NOT NULL,
  `Referee` varchar(45) NOT NULL,
  PRIMARY KEY (`MatchID`),
  UNIQUE KEY `matchID_UNIQUE` (`MatchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SELECT * FROM football.matchdetails;