from Methods import Methods

'''
Author: Jiaying Huang
Course: CST8333 Programming Language Research Project
Assignment: Final Project
Date: December 1, 2019

The purpose of this exercise is to practice inheritance in Python programming
This class is inherited from the Methods class and use all the functions defined in Method class
'''


class Main(Methods):

    def __init__(self):
        super().__init__()

    def option(self):
        # declare a global variable for this child class. The menu function defined in Method class.
        option = super().menu()

        while option is not '9':

            # This option allow user to reload the original data
            if option is '1':
                super().load()
                option = super().menu()

            # This option allow user to save the current dataframe to local
            if option is '2':
                super().export()
                option = super().menu()

            # This option presents all data in current dataframe
            if option is '3':
                super().displayAll()
                option = super().menu()

            # This option allow user to insert a single record in the dataframe which is located by its row index
            if option is '4':
                super().insert()
                option = super().menu()

            if option is '5':
                super().diaplaySingle()
                option = super().menu()

            # This option allow user to update a single record in the dataframe which is located by its row index
            if option is '6':
                super().update()
                option = super().menu()

            # This option allow user to delete a single record in the dataframe which is located by the value in the
            # column 'CheeseId'
            if option is '7':
                super().delete()
                option = super().menu()

            # This option allow user to search specific items in dataset
            if option is '8':
                super().search()
                option = super().menu()


if __name__ == '__main__':
    Main().option()
