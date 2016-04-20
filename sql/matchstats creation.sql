CREATE TABLE `matchstats` (
  `MatchID` varchar(45) NOT NULL,
  `FullTimeHomeGoals` int(11) NOT NULL,
  `FullTimeAwayGoals` int(11) NOT NULL,
  `FullTimeResults` varchar(1) NOT NULL,
  `HalfTimeHomeGoals` int(11) NOT NULL,
  `HalfTimeAwayGoals` int(11) NOT NULL,
  `HalfTimeResults` varchar(1) NOT NULL,
  `HomeShots` int(11) NOT NULL,
  `AwayShots` int(11) NOT NULL,
  `HomeShotsTarget` int(11) NOT NULL,
  `AwayShotsTarget` int(11) NOT NULL,
  `HomeFouls` int(11) NOT NULL,
  `AwayFouls` int(11) NOT NULL,
  `HomeCorners` int(11) NOT NULL,
  `AwayCorners` int(11) NOT NULL,
  `HomeYellow` int(11) NOT NULL,
  `AwayYellow` int(11) NOT NULL,
  `HomeRed` int(11) NOT NULL,
  `AwayRed` int(11) NOT NULL,
  UNIQUE KEY `MatchID_UNIQUE` (`MatchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
