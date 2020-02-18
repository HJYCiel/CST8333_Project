import pandas as pd
import sqlalchemy
from numpy import double
from sqlalchemy import MetaData, Table, insert, update
from sqlalchemy.orm import sessionmaker

'''
Author: Jiaying Huang
Course: CST8333 Programming Language Research Project
Assignment: Final Project
Date: December 1, 2019

The purpose of this exercise is to practice inheritance in Python programming
This class is the parent class which defined all the function that will be helpful to the child class (Main.class)
'''


class Methods:

    def __init__(self):

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
        self.engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/cheeseFactory')
        self.df.to_sql(con=self.engine, name='cheese_Table', if_exists='replace')
        self.result = ''
        self.res = {}

        # self.row_index = 200

    '''This function lists options for user to manipulate dataframe'''

    @staticmethod
    def menu():

        print("======Author: Jiaying Huang========\n=========MENU=========\n"
              "1. Reload the data from the dataset\n"
              "2. Export current dataframe to csv\n"
              "3. Display all the record\n"
              "4. Create a new record\n"
              "5. Select and display one record\n"
              "6. Select and edit one record\n"
              "7. delete one record\n"
              "8. Search for cheeses\n"
              "9. Quit\n")

        option = input("\nWhat would you like to do? (#)")
        return option

    '''This function asks user to enter the path of the original csv and load data into dataframe'''

    def load(self):
        self.__init__()
        print("Data has successfully reloaded!\n\n")
        return self.df

    '''This function exports the current dataframe to a csv and store in the user-chosen location'''

    def export(self):

        self.engine.execute(
            "SELECT \'CheeseId\',\'CheeseNameEn\',\'ManufacturerNameEn\',\'ManufacturerProvCode\',\'ManufacturingTypeEn\',\'WebSiteEn\',"
            "\'FatContentPercent\',\'MoisturePercent\',\'ParticularitiesEn\',\'FlavourEn\',\'CharacteristicsEn\',\'RipeningEn\',\'Organic\',"
            "\'CategoryTypeEn\',\'MilkTypeEn\',\'MilkTreatmentTypeEn\',\'RindTypeEn\',\'LastUpdateDate\' UNION ALL "
            "SELECT CheeseId,CheeseNameEn,ManufacturerNameEn,ManufacturerProvCode,ManufacturingTypeEn,WebSiteEn, "
            "FatContentPercent,MoisturePercent,ParticularitiesEn,FlavourEn,CharacteristicsEn,RipeningEn,Organic,"
            "CategoryTypeEn,MilkTypeEn,MilkTreatmentTypeEn,RindTypeEn,LastUpdateDate FROM cheese_Table "
            + "INTO OUTFILE \'" +
            input("Please enter the path to store the csv file (e.g /Users/jiaying/Desktop/):")
            + input("Name of the new file(e.g.canadianCheeseDirectory_updated.csv):") + "\'"
        )
        print("Data file saved on Desktop\n\n")

    '''This function lists all the record in current dataframe'''

    def displayAll(self):
        self.result = self.engine.execute("SELECT * FROM cheese_Table")

        for _r in self.result:
            print(_r)

    '''This function insert a record to the dataframe'''

    def insert(self):
        self.engine.connect()
        metadata = MetaData(bind=self.engine)
        cheese = Table('cheese_Table', metadata, autoload=True)
        i = insert(cheese)
        i = i.values({
            "CheeseId": input('CheeseId(Integer):'),
            "CheeseNameEn": input('CheeseNameEn:'),
            "ManufacturerNameEn": input('ManufacturerNameEn:'),
            "ManufacturerProvCode": input('ManufacturerProvCode:'),
            "ManufacturingTypeEn": input('ManufacturingTypeEn:'),
            "WebSiteEn": input('WebSiteEn:'),
            "FatContentPercent": input('FatContentPercent(Number):'),
            "MoisturePercent": input('MoisturePercent(Number):'),
            "ParticularitiesEn": input('ParticularitiesEn:'),
            "FlavourEn": input('FlavourEn:'),
            "CharacteristicsEn": input('CharacteristicsEn:'),
            "RipeningEn": input('RipeningEn:'),
            "Organic": input('Organic(Integer):'),
            "CategoryTypeEn": input('CategoryTypeEn:'),
            "MilkTypeEn": input('MilkTypeEn:'),
            "MilkTreatmentTypeEn": input('MilkTreatmentTypeEn:'),
            "RindTypeEn": input('RindTypeEn:'),
            "LastUpdateDate": input('LastUpdateDate')
        })
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.execute(i)
        session.commit()

    '''This function display a single user-chosen record'''

    def diaplaySingle(self):
        cheeseid = input("Please enter the CheeseId you would like to display: ")
        self.result = self.engine.execute("SELECT * FROM cheese_Table WHERE CheeseId = " + cheeseid)

        for _r in self.result:
            print(_r)

    '''This function update a single user-chosen record'''

    def update(self):

        self.engine.connect()

        cid = input("Please enter the CheeseId you would like to update: ")
        print("value cannot be empty")
        self.engine.execute(
            "UPDATE cheese_Table SET CheeseNameEn = '" + input('CheeseNameEn:') \
            + "',ManufacturerNameEn = '" + input('ManufacturerNameEn:') \
            + "', ManufacturerProvCode ='" + input('ManufacturerProvCode:') \
            + "', ManufacturingTypeEn = '" + input('ManufacturingTypeEn:') \
            + "', WebSiteEn = '" + input('WebSiteEn:') \
            + "', FatContentPercent = " + input('FatContentPercent(Number):') \
            + ", MoisturePercent = " + input('MoisturePercent(Number):') \
            + ", ParticularitiesEn = '" + input('ParticularitiesEn:') \
            + "', FlavourEn = '" + input('FlavourEn:') \
            + "', CharacteristicsEn = '" + input('CharacteristicsEn:') \
            + "', RipeningEn = '" + input('RipeningEn:') \
            + "', Organic = " + input('Organic(Integer):') \
            + ", CategoryTypeEn = '" + input('CategoryTypeEn:') \
            + "', MilkTypeEn = '" + input('MilkTypeEn:') \
            + "', MilkTreatmentTypeEn = '" + input('MilkTreatmentTypeEn:') \
            + "', RindTypeEn = '" + input('RindTypeEn:') \
            + "', LastUpdateDate = '" + input('LastUpdateDate: ') \
            + "' WHERE CheeseId = " + cid)

    '''This function delete a single user-chosen record'''

    def delete(self):
        cheeseid = input("Please enter the CheeseId you would like to drop: ")
        self.engine.execute("DELETE FROM cheese_Table WHERE CheeseId = " + cheeseid)

    '''This function search for specific cheeses that meet the condition and values which use entered'''

    def search(self):
        print("\nPlease input the values of the columns you would like to search and leave other columns BLANK.\n")

        # turns the user-input to a dictionary {key:value}
        Dict = {
            "CheeseId": input("CheeseId(Integer):"),
            "CheeseNameEn": input('CheeseNameEn:'),
            "ManufacturerNameEn": input('ManufacturerNameEn:'),
            "ManufacturerProvCode": input('ManufacturerProvCode:'),
            "ManufacturingTypeEn": input('ManufacturingTypeEn:'),
            "WebSiteEn": input('WebSiteEn:'),
            "FatContentPercent": input("FatContentPercent(Number):"),
            "MoisturePercent": input("MoisturePercent(Number):"),
            "ParticularitiesEn": input('ParticularitiesEn:'),
            "FlavourEn": input('FlavourEn:'),
            "CharacteristicsEn": input('CharacteristicsEn:'),
            "RipeningEn": input('RipeningEn:'),
            "Organic": input("Organic(Integer):"),
            "CategoryTypeEn": input('CategoryTypeEn:'),
            "MilkTypeEn": input('MilkTypeEn:'),
            "MilkTreatmentTypeEn": input('MilkTreatmentTypeEn:'),
            "RindTypeEn": input('RindTypeEn:'),
            "LastUpdateDate": input('LastUpdateDate:')
        }

        # remove the empty values in the dictionary (Dict)
        self.res = {k: v for k, v in Dict.items() if v is not ''}

        # if the input is a str, wrap the str with single quote mark
        query = ""
        for key, val in self.res.items():
            if type(val) is str:
                val="\'"+val+"\'"
            # Build up the 'WHERE' clause of the SQL statement
            query = query + key + " = " + val + " AND "

        # remove the last 5 element from query (str removed is " AND ")
        query = query[:-5]

        # search in the database and find the objects that matches the user-input conditions (matches the column and the values)
        self.result = self.engine.execute("SELECT * FROM cheese_Table WHERE " + query)

        #print out the found results
        print("\nRecords found:")
        for _r in self.result:
            print(_r)

        return [self.result,self.res.items()]
