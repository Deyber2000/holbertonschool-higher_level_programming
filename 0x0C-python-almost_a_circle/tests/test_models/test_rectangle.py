#!/usr/bin/python3
"""This module is for Rectangle unittests"""


import io
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    @classmethod
    def setUpClass(cls):
        """initializes class"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10, 3)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)
        cls.r4 = Rectangle(10, 10, 2, 3, 5)

    def tearDown(self):
        """tears down test"""
        pass

    def test_rec_class_type(self):
        """test class type"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_rec_inheritance(self):
        """test inheritance of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rec_no_arg(self):
        '''test Rectangle with no arguments'''
        with self.assertRaises(TypeError) as e:
            Rectangle()
        self.assertEqual(str(e.exception), "__init__() missing 2 required" +
                         " positional arguments: 'width' and 'height'")

    def test_rec_id(self):
        '''test Rectangle ids'''
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_rec_width(self):
        '''test Rectangle width'''
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_rec_height(self):
        '''test Rectangle height'''
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_rec_x(self):
        '''test Rectangle x'''
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.x, 0)

    def test_rec_y(self):
        '''test Rectangle y'''
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

    def test_width_type(self):
        '''test non-int widths'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("Thomas", 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(5.5, 10)

    def test_width_value(self):
        '''test out of range width'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 10)

    def test_height_type(self):
        '''test non-int heights'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(10, "Thomas")
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(10, 5.5)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(10, True)

    def test_height_value(self):
        '''test out of range heights'''
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(10, -10)

    def test_x_type(self):
        '''test non-int x'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 10, "Thomas")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 10, 10.5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 10, True)

    def test_x_value(self):
        '''test out of range x'''
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(10, 10, -10)

    def test_y_type(self):
        '''test non-int y'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 10, 8, "Thomas")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 10, 8, 8.8)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 10, 10, True)

    def test_y_value(self):
        '''test out of range y'''
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 10, 10, -10)

    def test_area_normal(self):
        '''test area'''
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)

    def test_str(self):
        '''test __str__ method'''
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.r4), "[Rectangle] (5) 2/3 - 10/10")

    def test_update(self):
        '''test update method'''
        r0 = Rectangle(10, 10, 0, 0, 1)
        self.assertEqual(str(r0), "[Rectangle] (1) 0/0 - 10/10")
        r0.update(4)
        self.assertEqual(str(r0), "[Rectangle] (4) 0/0 - 10/10")
        r0.update(8, 9, 10, 11, 12)
        self.assertEqual(str(r0), "[Rectangle] (8) 11/12 - 9/10")

    def test_update_no_args(self):
        '''test update method with no arguments'''
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_more_args(self):
        '''test update method with more than 5 arguments'''
        r = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 3/2 - 5/4")
        with self.assertRaisesRegex(IndexError, "list index out of range"):
            r.update(1, 2, 3, 4, 5, 6)

    def test_save_to_file(self):
        '''test save_to_file normally'''
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        r_dict = [r1, r2]
        Rectangle.save_to_file(r_dict)
        with open("Rectangle.json", "r") as f:
            dictionary = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(dictionary), f.read())

    def test_save_to_file_empty(self):
        '''test save_to_file with empty list'''
        r_dict = []
        Rectangle.save_to_file(r_dict)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        '''test save_to_file with None'''
        r_dict = None
        Rectangle.save_to_file(r_dict)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        '''test normal load'''
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        r_dict = [r1, r2]
        Rectangle.save_to_file(r_dict)
        load = Rectangle.load_from_file()
        self.assertTrue(type(load) is list)
        self.assertEqual(str(r1), str(load[0]))

    def test_create(self):
        '''test normal create'''
        ra = {"id": 1, "width": 10, "height": 2, "x": 5, "y": 6}
        rb = Rectangle.create(**ra)
        self.assertEqual(str(rb), '[Rectangle] (1) 5/6 - 10/2')
        self.assertIsNot(ra, rb)

    def test_display(self):
        '''test display with normal parameters'''
        rec = Rectangle(1, 1)
        hi = io.StringIO()
        with redirect_stdout(hi):
            rec.display()
        dis = '#\n'
        self.assertEqual(hi.getvalue(), dis)

    def test_display_no_param(self):
        '''test display without x and y'''
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_display_no_y(self):
        '''test display with one parameter'''
        rec = Rectangle(2, 2, 1)
        hi = io.StringIO()
        with redirect_stdout(hi):
            rec.display()
        dis = """\
 ##
 ##
"""
        self.assertEqual(hi.getvalue(), dis)

if __name__ == '__main__':
    unittest.main()
