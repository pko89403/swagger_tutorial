from django.test import TestCase
from .models import GuessNumber

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumber(name = 'apple',
                        text = 'pineapple')
        g.generate()
        
        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20)
        

