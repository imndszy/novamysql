# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import unittest

from db import (create_engine,close_engine,select_one,select_int,select,update,insert)

class DbTestCase(unittest.TestCase):

    def setUp(self):
        create_engine('szy', '123456', 'weixin', 'localhost', charset='utf8')
        update('drop table if exists test')
        update('create table test '
               '(id int auto_increment primary key,number int not null, name varchar(100) not null)')

    def tearDown(self):
        close_engine()

    def test_insert(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')

    def test_update(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')
        self.assertEqual(update("update test set number = 23 where name = 'ads' "),1,'test update fail')
        self.assertEqual(select_one("select number from test where name = 'ads'"), {u'number': 23},
                         'test select_one fail')

    def test_select_one(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')
        self.assertEqual(select_one("select number from test where name = 'ads'"),{u'number':21},'test select_one fail')

    def test_select_int(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')
        self.assertEqual(select_int("select number from test where name = 'ads'"),21,'test select_int fail')

    def test_select(self):
        self.assertEqual(insert('test', number=21, name='ads'), 1, 'test insert fail')
        self.assertEqual(select("select number from test where name = 'ads'"),[{u'number':21}],'test select fail')

if __name__ == "__main__":
    unittest.main()




