#!/usr/bin/python3
'''This module is for Square class tests'''


import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Tests for the Square class'''

    @classmethod
    def setUpClass(cls):
        '''initializes class'''
        Base._Base__nb_objects = 0
        cls.s1 = Square(10)
        cls.s2 = Square(2)
        cls.s3 = Square(10, 0, 0, 12)
        cls.s4 = Square(10, 2, 4, 5)

    def tearDown(self):
        '''tears down test'''
        pass

    def test_square_class_type(self):
        '''test class type'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_square_inheritance(self):
        '''test inheritance of Rectangle'''
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_id(self):
        '''test Square ids'''
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 12)

    def test_square_size(self):
        '''test Square size'''
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 10)

    def test_square_normal(self):
        '''test normal Square'''
        s = Square(1, 2)
        self.assertEqual(s.size, 1)

    def test_square_3(self):
        '''test Square with 3 parameters'''
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_4(self):
        '''test Square with 4 parameters'''
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_square_string_1(self):
        '''test Square with string'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("1")

    def test_square_string_2(self):
        '''test Square with string'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, "2")

    def test_square_string_3(self):
        '''test Square with string'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, "3")

    def test_square_neg_1(self):
        '''test Square with negative value'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-1)

    def test_square_neg_2(self):
        '''test Square with negative value'''
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(1, -2)

    def test_square_neg_3(self):
        '''test Square with negative value'''
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(1, 2, -3)

    def test_square_zero_1(self):
        '''test Square with zero value'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    def test_square_zero_2(self):
        '''test Square with zero value'''
        s = Square(1, 0)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)

    def test_square_zero_3(self):
        '''test Square with zero value'''
        s = Square(1, 2, 0)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_square_zero_4(self):
        '''test Square with zero value'''
        s = Square(1, 2, 3, 0)
        self.assertEqual(s.id, 0)

    def test_square_str_1(self):
        '''test __str__ representation of Square'''
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(str(self.s4), "[Square] (5) 2/4 - 10")

    def test_square_to_dict(self):
        '''test Square to_dictionary()'''
        s = Square(1, 2, 3, 4)
        s_todict = s.to_dictionary()
        self.assertTrue(type(s_todict) is dict)

    def test_square_update_1(self):
        '''test Square update()'''
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")
        s.update()
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_square_update_2(self):
        '''test Square update(89)'''
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_update_3(self):
        '''test Square update(89, 1)'''
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_update_4(self):
        '''test Square update(89, 1, 2)'''
        s = Square(4, 3, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 3/2 - 4")
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/2 - 1")

    def test_square_update_5(self):
        '''test Square update(89, 1, 2, 3)'''
        s = Square(4, 3, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 3/2 - 4")
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_update_6(self):
        '''test Square update(**{ 'id': 89 })'''
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")
        s.update(**{'id': 89})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_update_7(self):
        '''test Square update(**{ 'id': 89, 'size': 1 })'''
        s = Square(4, 3, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 3/2 - 4")
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), "[Square] (89) 3/2 - 1")

    def test_square_update_8(self):
        '''test update(**{ 'id': 89, 'size': 1, 'x': 2 })'''
        s = Square(4, 3, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 3/2 - 4")
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/2 - 1")

    def test_square_update_9(self):
        '''test update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })'''
        s = Square(4, 3, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 3/2 - 4")
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_create_1(self):
        '''test Square.create(**{ 'id': 89 })'''
        s1 = {'id': 89}
        s2 = Square.create(**s1)
        self.assertEqual(str(s2), '[Square] (89) 0/0 - 6')
        self.assertIsNot(s1, s2)

    def test_square_create_2(self):
        '''Square.create(**{ 'id': 89, 'size': 1 })'''
        s1 = {'id': 89, 'size': 1}
        s2 = Square.create(**s1)
        self.assertEqual(str(s2), '[Square] (89) 0/0 - 1')

    def test_square_create_3(self):
        '''Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })'''
        s1 = {'id': 89, 'size': 1, 'x': 2}
        s2 = Square.create(**s1)
        self.assertEqual(str(s2), '[Square] (89) 2/0 - 1')

    def test_square_create_4(self):
        '''Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })'''
        s1 = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s2 = Square.create(**s1)
        self.assertEqual(str(s2), '[Square] (89) 2/3 - 1')

    def test_square_save_to_file_none(self):
        '''test Square save_to_file with None'''
        with self.assertRaises(TypeError) as e:
            Square.save_to_file()
        s = ("save_to_file() missing 1 required positional" +
             " argument: 'list_objs'")
        self.assertEqual(str(e.exception), s)

    def test_square_save_to_file_empty(self):
        '''test Square save_to_file with []'''
        s_dict = []
        Square.save_to_file(s_dict)
        with open('Square.json', 'r') as f:
            self.assertEqual('[]', f.read())

    def test_square_save_to_file_normal(self):
        '''test Square save_to_file with normal case'''
        s1 = Square(1)
        s2 = Square(1, 2, 3, 4)
        s_dict = [s1, s2]
        Square.save_to_file(s_dict)
        with open('Square.json', 'r') as f:
            dictionary = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(dictionary), f.read())

    def test_square_load_from_file_no_file(self):
        '''test load_from_file with no file'''
        load = Square.load_from_file()
        self.assertTrue(type(load) is list)

    def test_square_load_from_file_with_file(self):
        '''test load_from_file with file'''
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        s_dict = [s1, s2]
        Square.save_to_file(s_dict)
        load = Square.load_from_file()
        self.assertTrue(type(load) is list)
        self.assertEqual(str(s1), str(load[0]))

if __name__ == '__main__':
    unittest.main()
