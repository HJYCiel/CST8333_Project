import os
import unittest
from unittest.mock import patch, Mock, MagicMock

import pandas as pd
import sqlalchemy
from pandas.util.testing import assert_frame_equal

import Methods
from Main import Main
from Methods import Methods

'''
Author: Jiaying Huang
Course: CST8333 Programming Language Research Project
Assignment: Final Project
Date: December 1, 2019

The purpose of this test file is to test if the original program ran and generate the expected results
'''


class MyTestCase(unittest.TestCase):
    print("Testing Main.py by Jiaying Huang............\n")

    def setUp(self):
        columns = ['CheeseId',
                   'CheeseNameEn',
                   'ManufacturerNameEn',
                   'ManufacturerProvCode',
                   'ManufacturingTypeEn',
                   'WebSiteEn',
                   'FatContentPercent',
                   'MoisturePercent',
                   'ParticularitiesEn',
                   'FlavourEn',
                   'CharacteristicsEn',
                   'RipeningEn',
                   'Organic',
                   'CategoryTypeEn',
                   'MilkTypeEn',
                   'MilkTreatmentTypeEn',
                   'RindTypeEn',
                   'LastUpdateDate']

        self.csv_path = input("Please enter the path of the csv file (e.g. "
                              "/Users/jiaying/Desktop/canadianCheeseDirectory.csv): ")
        data = pd.read_csv(self.csv_path, usecols=columns, index_col=None, squeeze=True, header=0).to_dict()
        self.df = pd.DataFrame(data)
        self.engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/testdb')
        # self.connection = self.engine.connect()
        # self.connection.execute("CREATE DATABASE IF NOT EXISTS testdb")
        self.df.to_sql(con=self.engine, name='cheese_Table', if_exists='replace')

    def test_insert(self):

        old = self.engine.execute("SELECT count(*) FROM cheese_Table")
        Main().insert()
        new = self.engine.execute("SELECT count(*) FROM cheese_Table")
        self.assertNotEqual(old, new)

    def test_search(self):

        # get the returned values from search() in Methods class
        list_res = Methods().search()

        # turn the resultproxy (var self.result in search() ) object into a dictionary called dict_res1
        i = 0
        dict_res1 = {}
        for _r in list_res[0]:
            dict_res1[i] = _r
            i += 1

        # compared the values in the dict_res1 with var self.res in search() under the same key
        s = 0
        while s < i:
            for key, val in list_res[1]:
                self.assertEqual(val, dict_res1[i][key])
            s += 1


if __name__ == '__main__':
    unittest.main()
