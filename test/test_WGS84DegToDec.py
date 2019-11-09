import unittest
from fonctions.WGS84DegToDec import WGS84DegToDec

class WGS84Deg_Test(unittest.TestCase):
    """
        Tests automatiques pour la fonction WGS84DegToDec qui convertit les degrés WGS84 sexadécimal en décimal
    """

    def test_1(self):
        """38.8897 = 38 53' 23'' """
        dec = WGS84DegToDec(38, 53, 23)
        self.assertEqual(round(dec, 3), 38.89)

    def test_2(self):
        """-77.0089 = -77 00' 32'' """
        dec = WGS84DegToDec(77, 00, 32)
        self.assertEqual(round(dec, 1), 77.00)

    def test_3(self):
        """47.494128 = 47 29' 39''"""
        dec = WGS84DegToDec(47, 29, 39)
        self.assertEqual(round(dec, 2), 47.49)

    def test_4(self):
        """3.043041 = 3 2' 35''"""
        dec = WGS84DegToDec(3, 2, 35)
        self.assertEqual(round(dec, 2), 3.04)


if __name__ == '__main__':
    unittest.main()
