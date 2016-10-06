# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import unittest
import logging

from db import (create_engine,select,update,insert)

class DbTestCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        create_engine('szy', '123456', 'weixin', 'localhost', charset='utf8')

    def tearDown(self):
        pass

    def test_insert(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')

    def test_update(self):
        pass

    def test_select(self):
        pass





