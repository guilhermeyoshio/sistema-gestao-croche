from django.test import TestCase

class CalculoInsumoTest(TestCase):
    def test_calculo_custo_total(self):
        metros = 150
        custo = 0.10
        total = metros * custo
        self.assertEqual(total, 15.0)