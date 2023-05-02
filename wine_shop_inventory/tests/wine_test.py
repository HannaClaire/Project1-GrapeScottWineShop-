import unittest
from models.wine import Wine
from models.producer import Producer



class TestWine(unittest.TestCase):

    def setUp(self):
        self.producer1 = Producer("FancyPants", id)
        self.wine1 = Wine("Pinot Gris", "White - medium/full-bodied, Notes & flavours: delicate/floral aromatics; round feel, nutty/spicy, pears/melon on palette.", 6, 9, 18, self.producer1.id)
        self.wine2 = Wine("Pinot Noir", "Red - light/medium-bodied, Notes & flavours: red fruits/spicey aromas, red fruits, clove, hibiscus, umami on palette.", 15, 10, 20, self.producer1.id)
        self.wine3 = Wine("Pinot Blanc", "White - medium/full-bodies, Notes & flavours: floral aromas, round feel, peaches/pears/almonds and slight minerality on the palette.", 0, 14, 22, self.producer1.id)
    
    
    
    def test_wine_has_name(self):
        self.assertEqual("Pinot Gris", self.wine1.name)
    
    def test_has_selling_price(self):
        self.assertEqual(18, self.wine1.selling_price)

    def test_has_stock_count(self):
        self.assertEqual(6, self.wine1.stock_quantity)

    def test_has_buying_cost(self):
        self.assertEqual(9, self.wine1.buying_cost)

    def test_producer_has_name(self):
        self.assertEqual("FancyPants", self.producer1.name)
    
    def test_get_markup(self):
        mark_up = (self.wine1.get_markup())
        self.assertEqual(100, mark_up)
