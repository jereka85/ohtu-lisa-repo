import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):        
        reader = PlayerReaderStub()
        self.stats = StatisticsService(reader)

    def test_team(self):
        edm = self.stats.team("EDM")
        edm_str = [str(p) for p in edm]

        vastaus = [
            str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Gretzky", "EDM", 35, 89))
        ]
                
        self.assertEqual(edm_str, vastaus)

    def test_search(self):
        vastaus = str(Player("Yzerman", "DET", 42, 56))
        etsi_yzer = self.stats.search("Yzerman")
        etsi_tyhja = self.stats.search("Joulupukki")
        
        self.assertEqual(None, etsi_tyhja)
        self.assertEqual(str(etsi_yzer), vastaus)

    def test_top(self):

        vastaus = [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Lemieux", "PIT", 45, 54)),
            str(Player("Yzerman", "DET", 42, 56))
            ]

        top_3 = self.stats.top(3)
        top_3_str = [str(p) for p in top_3]

        self.assertEqual(top_3_str, vastaus)
