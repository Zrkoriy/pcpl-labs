import math
import unittest

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestFigures(unittest.TestCase):

    def test_rectangle(self):
        r = Rectangle(2, 3, 'синего')
        self.assertEqual(r.square(), 6)
        self.assertEqual(r.fc.color, 'синего')

    def test_circle(self):
        c = Circle(2, 'зеленого')
        self.assertAlmostEqual(c.square(), 4 * math.pi)

    def test_square(self):
        s = Square(4, 'красного')
        self.assertEqual(s.square(), 16)
        self.assertEqual(s.get_figure_type(), 'Квадрат')
        self.assertIsInstance(s, Rectangle)


if __name__ == '__main__':
    unittest.main()
