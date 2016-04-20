import requests as req
import pymysql as sql


class DBComms():

    def __init__(self, host='localhost', user='Apps', password='Operator', db='football'):

        self.conn = sql.connect(host=host, user=user, password=password, db=db)

        self.matchDetailsQuery = "INSERT INTO matchdetails " \
            "(MatchId, Division, Season, MatchNo, MatchDate, HomeTeam, AwayTeam, Referee) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        self.matchstatsQuery = "INSERT INTO matchstats " \
        "(MatchId, FullTimeHomeGoals, FullTimeAwayGoals, FullTimeResults, HalfTimeHomeGoals, "\
            "HalfTimeAwayGoals, HalfTimeResults, HomeShots, AwayShots, HomeShotsTarget, " \
                "AwayShotsTarget, HomeFouls, AwayFouls, HomeCorners, "\
                    "AwayCorners, HomeYellow, AwayYellow, HomeRed, AwayRed) "\
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    def update_from_links(self, links, season):

        with self.conn.cursor() as cur:
            for link in links:
                if link.split('/')[1] in season:
                    tempdata = str(req.get('http://www.football-data.co.uk/' + link).content, encoding='utf-8')
                    tempdata = tempdata.split('\n')
                    data = []
                    for d in tempdata:
                        data.append(d.split(','))

                    for n, record in enumerate(data):
                        if n > 0:
                            try:
                                if len(record)>0:
                                    MatchId = record[0] + link.split('/')[1] + str(n)
                                    Season = link.split('/')[1]
                                    Division = record[0]
                                    MatchDate = '/'.join(record[1].split('/')[::-1])
                                    HomeTeam = record[2]
                                    AwayTeam = record[3]
                                    Referee = record[10]
                                    cur.execute(self.matchDetailsQuery, (MatchId, Division, Season, str(n), MatchDate, HomeTeam, AwayTeam, Referee))

                            except Exception as e:
                                print(e)

                            try:
                                if len(record)>0:
                                    MatchId = record[0] + link.split('/')[1] + str(n)
                                    FullTimeHomeGoals = str(record[4])
                                    FullTimeAwayGoals = str(record[5])
                                    FullTimeResults = str(record[6])
                                    HalfTimeHomeGoals = str(record[7])
                                    HalfTimeAwayGoals = str(record[8])
                                    HalfTimeResults = str(record[9])
                                    HomeShots = str(record[11])
                                    AwayShots = str(record[12])
                                    HomeShotsTarget = str(record[13])
                                    AwayShotsTarget = str(record[14])
                                    HomeFouls = str(record[15])
                                    AwayFouls = str(record[16])
                                    HomeCorners = str(record[17])
                                    AwayCorners = str(record[18])
                                    HomeYellow = str(record[19])
                                    AwayYellow = str(record[20])
                                    HomeRed = str(record[21])
                                    AwayRed = str(record[22])

                                    cur.execute(self.matchstatsQuery, (MatchId, FullTimeHomeGoals, FullTimeAwayGoals, FullTimeResults, HalfTimeHomeGoals,
                                        HalfTimeAwayGoals, HalfTimeResults, HomeShots, AwayShots, HomeShotsTarget, AwayShotsTarget, HomeFouls, AwayFouls, HomeCorners,
                                        AwayCorners, HomeYellow, AwayYellow, HomeRed, AwayRed))

                            except Exception as e:
                                print(e)

                    self.conn.commit()

if __name__ == '__main__':

    dbcomms = DBComms()
    dbcomms.update_from_links(['mmz4281/1516/E0.csv', 'mmz4281/1516/E1.csv'])