"""
Python Version : python 3.5 or higher
Description : Python command line utility to perform all actions needed in MySQL Database.
Get Couloum names of a table
Check whether entry exists in a table
Add entry to a table
read a file a predefined

"""

from datetime import date
import mysql.connector



class Mysql_actions():
    def __init__(self,query = None):
        self.mysqlDBServerIP = "10.182.197.79"
        self.mydb=mysql.connector.connect(host=self.mysqlDBServerIP,user="root",passwd="root", database="LabToolDB",port=3308,charset="utf8",use_pure=True)
        self.mycursor = self.mydb.cursor()
        #self.tablename = tablename
        self.query = query
        print ("\n==========connected==========\n")
        

    def get_coloums(self):
        self.mycursor.execute(self.query)
        print ("==========command is ==========\n",self.query)
        print ("=============================")
        self.pdd_file_list = (list(self.mycursor.column_names))
        return (self.pdd_file_list)

    def check_entry_exists(self):
        print ("==========command is ==========\n",self.query)
        print ("=============================")
        self.mycursor.execute(self.query)
        myresult = self.mycursor.fetchall()
        return (myresult)

    def add_entry_mysqldb(self):
        print ("==========command is ==========\n",self.query)
        print ("=============================")
        self.mycursor.execute(self.query)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) affected")
        print ("updation done...")

