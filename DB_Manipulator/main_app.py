import os
import sqlite3
import pandas as pd
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

db_path = []
current_table = []
class Ui_MainWindow(object):
    '''My code begins on line 191'''
    def setupUi(self, MainWindow):
        '''Sets up the UI'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 486)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 40, 521, 391))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.view = QtWidgets.QListWidget(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(550, 60, 151, 221))
        self.view.setObjectName("view")
        self.open_db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_db_btn.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.open_db_btn.setObjectName("open_db_btn")
        self.edit_db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_db_btn.setGeometry(QtCore.QRect(120, 10, 81, 23))
        self.edit_db_btn.setObjectName("edit_db_btn")
        self.close_db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_db_btn.setGeometry(QtCore.QRect(230, 10, 81, 23))
        self.close_db_btn.setObjectName("close_db_btn")
        self.outside_table = QtWidgets.QLabel(self.centralwidget)
        self.outside_table.setGeometry(QtCore.QRect(540, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.outside_table.setFont(font)
        self.outside_table.setText("Choose a .db file...")
        self.outside_table.setObjectName("outside_table")
        self.rows = QtWidgets.QLabel(self.centralwidget)
        self.rows.setGeometry(QtCore.QRect(540, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.rows.setFont(font)
        self.rows.setText("")
        self.rows.setObjectName("rows")
        self.columns = QtWidgets.QLabel(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(610, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.columns.setFont(font)
        self.columns.setText("")
        self.columns.setObjectName("columns")
        self.inside_table = QtWidgets.QLabel(self.centralwidget)
        self.inside_table.setGeometry(QtCore.QRect(540, 11, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inside_table.setFont(font)
        self.inside_table.setText("")
        self.inside_table.setObjectName("inside_table")
        self.rename_col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rename_col_btn.setGeometry(QtCore.QRect(710, 120, 101, 21))
        self.rename_col_btn.setObjectName("rename_col_btn")
        self.rename_input = QtWidgets.QLineEdit(self.centralwidget)
        self.rename_input.setGeometry(QtCore.QRect(710, 60, 101, 20))
        self.rename_input.setObjectName("rename_input")
        self.del_col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_col_btn.setGeometry(QtCore.QRect(710, 210, 101, 21))
        self.del_col_btn.setObjectName("del_col_btn")
        self.del_row_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_row_btn.setGeometry(QtCore.QRect(550, 290, 111, 23))
        self.del_row_btn.setObjectName("del_row_btn")
        self.text_type_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.text_type_rb.setGeometry(QtCore.QRect(690, 320, 82, 16))
        self.text_type_rb.setObjectName("text_type_rb")
        self.int_type_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.int_type_rb.setGeometry(QtCore.QRect(690, 340, 82, 17))
        self.int_type_rb.setObjectName("int_type_rb")
        self.real_type_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.real_type_rb.setGeometry(QtCore.QRect(690, 360, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.real_type_rb.setFont(font)
        self.real_type_rb.setObjectName("real_type_rb")
        self.table_name = QtWidgets.QLineEdit(self.centralwidget)
        self.table_name.setGeometry(QtCore.QRect(550, 330, 111, 20))
        self.table_name.setObjectName("table_name")
        self.create_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_table_btn.setGeometry(QtCore.QRect(550, 360, 111, 23))
        self.create_table_btn.setObjectName("create_table_btn")
        self.add_col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_col_btn.setGeometry(QtCore.QRect(550, 410, 111, 23))
        self.add_col_btn.setObjectName("add_col_btn")
        self.or_info = QtWidgets.QLabel(self.centralwidget)
        self.or_info.setGeometry(QtCore.QRect(580, 390, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        font.setItalic(True)
        self.or_info.setFont(font)
        self.or_info.setObjectName("or_info")
        self.blob_type_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.blob_type_rb.setGeometry(QtCore.QRect(690, 380, 82, 17))
        self.blob_type_rb.setObjectName("blob_type_rb")
        self.data_type_info = QtWidgets.QLabel(self.centralwidget)
        self.data_type_info.setGeometry(QtCore.QRect(690, 300, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.data_type_info.setFont(font)
        self.data_type_info.setObjectName("data_type_info")
        self.show_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_table_btn.setGeometry(QtCore.QRect(710, 260, 101, 21))
        self.show_table_btn.setObjectName("show_table_btn")
        self.rename_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rename_table_btn.setGeometry(QtCore.QRect(710, 90, 101, 21))
        self.rename_table_btn.setObjectName("rename_table_btn")
        self.exit_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_table_btn.setGeometry(QtCore.QRect(450, 10, 81, 21))
        self.exit_table_btn.setObjectName("exit_table_btn")
        self.del_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_table_btn.setGeometry(QtCore.QRect(710, 180, 101, 21))
        self.del_table_btn.setObjectName("del_table_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(710, 410, 101, 23))
        self.exit_btn.setObjectName("exit_btn")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(340, 10, 81, 21))
        self.refresh_btn.setObjectName("refresh_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

####################Button actions####################

        self.open_db_btn.clicked.connect(lambda: self.open_db(MainWindow))
        self.edit_db_btn.clicked.connect(lambda: self.edit_db(MainWindow))
        self.close_db_btn.clicked.connect(lambda: self.close_db(MainWindow))
        self.refresh_btn.clicked.connect(lambda: self.refresh(MainWindow))
        self.exit_table_btn.clicked.connect(lambda: self.exit_table(MainWindow))

        self.rename_table_btn.clicked.connect(lambda: self.rename_table(MainWindow))
        self.rename_col_btn.clicked.connect(lambda: self.rename_col(MainWindow))
        self.del_table_btn.clicked.connect(lambda: self.delete_table(MainWindow))
        self.del_col_btn.clicked.connect(lambda: self.delete_col(MainWindow))
        self.show_table_btn.clicked.connect(lambda: self.show_table(MainWindow))

        self.del_row_btn.clicked.connect(lambda: self.del_row(MainWindow))
        self.create_table_btn.clicked.connect(lambda: self.create_table(MainWindow))
        self.add_col_btn.clicked.connect(lambda: self.add_column(MainWindow))

        self.exit_btn.clicked.connect(MainWindow.close)

####################Open DB functions####################

    def search_file(self):
        '''Searches for .db file'''
        raw_path = QFileDialog.getOpenFileName(MainWindow, 'Open DB', os.getenv('HOME'), 'DB(*.db)')
        path = str(raw_path).replace("(", "").replace(")", "").replace(", 'DB*.db'", "").replace("'", "")
        db_path.append(path)

    def sql_tables(self):
        '''Gathers all SQLite table names from the .db file and inserts them into the "view" QListWidget'''
        raw_names = []
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        for name in c.fetchall():
            raw_names.append(name)
        shownames = [str(name).replace("(", "").replace(")", "").replace(",", "").replace("'", "") for name in raw_names]
        self.view_insert(shownames)

    def view_insert(self, list):
        '''Inserts items from a list into the view listwidget'''
        self.view.clear()
        for i in list:
            self.view.addItem(i)
        self.view.setCurrentRow(0)

    def open_db(self, MainWindow): ###Could combine EXit Table function and Open DB function
        '''Open DB Function'''
        try:
            if len(db_path) > 0:
                raise IndexError
            self.search_file()
            self.sql_tables()
            self.outside_table.setText("Choose a table...")
        except IndexError:
            pass

####################Show SQLite table functions####################

    def show_table(self, MainWindow):
        '''Sets up the table strucutre and data'''
        try:
            if len(current_table) == 0:
                selected = self.view.currentRow()
                sql_table = self.view.item(selected).text()
                current_table.append(sql_table)
                self.structure(sql_table)
                self.messages(sql_table)
            else:
                self.structure(current_table[0])
                self.messages(current_table[0])
        except AttributeError:
            pass

    def cols_list(self):
        '''Returns a list of all columns in a SQLite table'''
        cols = []
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        data = c.execute("SELECT * FROM {}".format(current_table[0]))
        for column in c.description:
            cols.append(column[0])
        return cols

    def structure(self, sql):
        '''Sets up the structure of the tablewidget'''
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        cols = self.cols_list()
        self.table.setColumnCount(len(cols))
        self.table.setHorizontalHeaderLabels(cols)
        self.table_data(c)
        self.view_reset(self.col_type_list(sql, cols))

    def table_data(self, c):
        data = c.execute("SELECT * FROM {}".format(current_table[0]))
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def view_reset(self, zipped):
        '''Fills the view listwidget with column names and data types from a zipped list'''
        self.view.clear()
        for col, type in zipped:
            self.view.addItem("{} ({})".format(col, type))
        self.view.setCurrentRow(0)

    def col_type_list(self, table, columns):
        '''Returns zipped list of column names and data types'''
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        types = []
        c.execute("PRAGMA TABLE_INFO({})".format(table))
        for t in c.fetchall():
            types.append(t[2])
        return zip(columns, types)

    def messages(self, table):
        '''Sets the labels above the listwidget, revealing information about the SQLite table being used'''
        self.inside_table.setText("{}".format(table))
        self.rows.setText("Rows = {}".format(self.table.rowCount()))
        self.columns.setText("Columns = {}".format(self.table.columnCount()))
        self.outside_table.setText("")

####################Rename table/column functions####################

    def view_grab(self, list):
        '''Fills a list with all information from the view listwidget'''
        for index in range(self.view.count()):
            r = self.view.item(index).text()
            list.append(r)

    def rename_col(self, MainWindow):
        '''Renames columns from the SQLite table without changing the data within the columns'''
        try:
            if len(db_path) == 0 or len(current_table) == 0:
                pass
            else:
                old_cols = []
                if self.rename_input.text() == '': #if the column is empty, the window will not crash
                    raise AttributeError
                self.view_grab(old_cols)
                old = [c.replace("(", "").replace(")", "") for c in old_cols]
                self.sql_col_change(self.col_name_switch(), old)
                self.rename_input.clear()
                cols = self.cols_list()
                self.view_reset(self.col_type_list(current_table[0], cols))
        except AttributeError:
            pass

    def rename_table(self, MainWindow):
        '''Renames SQLite table and refreshes information in the view listwidget'''
        try:
            if len(current_table) == 0:
                selected = self.view.currentRow()
                old_name = self.view.item(selected).text()
                raw = self.rename_input.text()
                if raw == "":
                    raise AttributeError
                new_name = raw.replace(" ", "_")
                self.sql_rename_table(old_name, new_name)
                self.rename_input.clear()
                self.view.clear()
                self.sql_tables()
            else:
                pass
        except AttributeError:
            pass

    def sql_rename_table(self, old_name, new_name):
        '''Renames the SQLite table, with old_name parameter being the table selected'''
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        with conn:
            c.execute("ALTER TABLE {} RENAME TO {}".format(old_name, new_name))

    def col_name_switch(self):
        '''Returns a tuple of columns for new table'''
        try:
            cols = []
            selected = self.view.currentRow()
            old_col = self.view.item(selected).text() #the selected column from the UI
            raw = self.rename_input.text() #grabs the user's input for the new name
            input = raw.replace(" ", "_")
            new_col = self.attach_types(old_col, input)
            self.view_grab(cols)
            almost = [new_col if c == old_col else c for c in cols] #switching the desired column to the new name only---everything else stays the same
            self.view_insert(almost)
            new_cols = [c.replace("(", "").replace(")", "") for c in almost]
            return tuple(new_cols) #converts into a tuple, for creating a new table
        except ValueError: #keeps the program from crashing
            pass

    def attach_types(self, old, input):
        '''Returns a string of correct form for list'''
        type = old.partition(" ")
        new = input + " {}".format(type[2])
        return new

    def no_types(self, cols):
        '''Strips items in the list from uppercase types'''
        col_names = []
        for c in cols:
            name = c.partition(" ")
            col_names.append(name[0])
        return col_names

    def sql_col_change(self, col_tuple, no_types):
        '''This function is for the Delete Column and Rename Column option.
        The "col_tuple" parameter is for updated columns w/ data types, and
        "no_types" parameter is for the same columns but without data types'''
        try:
            conn = sqlite3.connect(db_path[0])
            c = conn.cursor()
            table = current_table[0]
            cols = ", ".join(str(i) for i in no_types)
            new_columns = ", ".join(str(i) for i in col_tuple) #translates the list of columns into usable strings
            with conn: #must create a new table, rename the columns with desired name changes, then copy the data from the old table into the new table, drop the old table, then rename this table to the old table's name
                c.execute('CREATE TABLE IF NOT EXISTS backup({})'.format(new_columns)) #creates the correct, corresponding column names of the "new" table
                c.execute("INSERT INTO backup SELECT {} FROM {}".format(cols, table))
                c.execute("DROP TABLE {}".format(table))
                c.execute("ALTER TABLE backup RENAME TO {}".format(table))
        except IndexError:
            pass

####################Delete table/column functions####################

    def view_del(self):
        '''Returns a list of all columns, except for the deleted column'''
        view_data = []
        selected = self.view.currentRow()
        x = self.view.item(selected).text()
        self.view_grab(view_data)
        view_data.remove(x)
        data = [d.replace("(", "").replace(")", "") for d in view_data]
        return data

    def delete_col(self, MainWindow):
        '''Deletes the SQLite column and refreshes the view listwidget'''
        if len(current_table) > 0:
            new_cols = tuple(self.view_del()) #for creating the table
            no_types = self.no_types(new_cols)
            self.sql_col_change(new_cols, no_types)
            self.view_reset(self.col_type_list(current_table[0], self.cols_list()))
            self.columns.setText("Columns = {}".format(self.view.count()))
        else:
            pass

    def delete_table(self, MainWindow):
        '''Deletes the SQLite table and refreshes the view listwidget'''
        try:
            if len(current_table) == 0:
                self.del_sql()
                self.view.clear()
                self.sql_tables()
            elif len(db_path) == 0:
                pass
            else:
                pass
        except IndexError:
            pass

    def del_sql(self):
        '''Deletes the selected SQLite table'''
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        selected = self.view.currentRow()
        table = self.view.item(selected).text()
        with conn:
            c.execute("DROP TABLE " + table)


####################Create table/column functions####################

    def create_table(self, MainWindow):
        '''Creates an SQLite table and refreshes the view listwidget'''
        try:
            if len(current_table) > 0:
                pass
            else:
                conn = sqlite3.connect(db_path[0])
                c = conn.cursor()
                if self.table_name.text() == "":
                    raise IndexError
                raw = self.table_name.text()
                table = raw.replace(" ", "_")
                with conn:
                    c.execute("CREATE TABLE IF NOT EXISTS {} (temp_col TEXT)".format(table))
                self.view.clear()
                self.sql_tables()
        except IndexError:
            pass

    def add_column(self, MainWindow):
        '''Adds a column w/ data type to the SQLite table being used and refreshes the view listwidget '''
        try:
            if len(db_path) == 0 or len(current_table) == 0:
                raise AttributeError
            raw = self.table_name.text()
            if raw == "":
                raise AttributeError
            col_name = raw.replace(" ", "_")
            if self.text_type_rb.isChecked():
                self.add_col(col_name, 'TEXT')
            elif self.int_type_rb.isChecked():
                self.add_col(col_name, 'INTEGER')
            elif self.real_type_rb.isChecked():
                self.add_col(col_name, 'REAL')
            elif self.blob_type_rb.isChecked():
                self.add_col(col_name, 'BLOB')
        except AttributeError:
            pass


    def add_col(self, col_name, type):
        '''Adds a column w/ data type to the SQLite table being used'''
        conn = sqlite3.connect(db_path[0])
        c = conn.cursor()
        table = current_table[0]
        with conn:
            c.execute("ALTER TABLE {} ADD COLUMN {} {}".format(table, col_name, type))
        self.view_reset(self.col_type_list(current_table[0], self.cols_list()))
        self.columns.setText("Columns = {}".format(self.view.count()))
        self.table_name.clear()

####################Exit table functions####################

    def exit_messages(self, option):
        '''Resets the labels when exiting the current SQLite table'''
        if option == "exit_table":
            self.outside_table.setText("Choose a table...")
        elif option == "close_db":
            self.outside_table.setText("Choose a .db file...")
        self.inside_table.setText("")
        self.rows.setText("")
        self.columns.setText("")

    def clearing(self):
        '''Clears the widgets below when exiting out of the current SQLite table'''
        self.table.setRowCount(0)
        self.table.clear()
        self.view.clear()
        current_table.clear()

    def exit_table(self, MainWindow):
        try:
            self.clearing()
            self.exit_messages("exit_table")
            self.sql_tables()
        except IndexError:
            pass

####################Close DB functions####################

    def close_db(self, MainWindow):
        '''Exits out of the current .db file being used'''
        try:
            if len(db_path) == 0:
                raise IndexError
            sqlite3.connect(db_path[0]).close()
            self.clearing()
            db_path.clear()
            self.exit_messages("close_db")
        except IndexError:
            pass

####################Save DB functions####################

    def edit_db(self, MainWindow):
        '''Replaces all data from the original SQLite table with data from the tablewidget'''
        try:
            conn = sqlite3.connect(db_path[0])
            c = conn.cursor()
            table_name = current_table[0]
            self.table_to_csv()
            self.csv_to_sql(c, conn, table_name)
            self.table_data(c)
            self.messages(table_name)
            self.view_reset(self.col_type_list(table_name, self.cols_list()))
            self.clear_csv()
        except IndexError:
            pass

    def clear_csv(self):
        '''Clears the csv file to avoid any potential complications'''
        with open("transfer.csv", "w") as file:
            writer = csv.writer(file, dialect='excel')
            writer.writerow('')

    def table_to_csv(self):
        '''Transfers all tablewidget data to the transfer.csv file'''
        pre_headers = []
        self.view_grab(pre_headers)
        headers = self.no_types(pre_headers) #returns a list
        with open("transfer.csv", "w") as file:
            writer = csv.writer(file, dialect='excel')
            writer.writerow(headers)
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)

    def csv_to_sql(self, c, conn, table):
        '''Transfers csv file data to a "new" SQLite table'''
        df = pd.read_csv('transfer.csv')
        with conn:
            c.execute("DROP TABLE {}".format(table))
        df.to_sql(table, conn, index=False)

####################Refresh functions####################

    def refresh(self, MainWindow):
        '''Refreshes the tablewidget and view listwidget'''
        if len(current_table) == 0:
            pass
        else:
            table = current_table[0]
            self.table.setRowCount(0)
            self.table.clear()
            self.view.clear()
            self.structure(table)
            self.messages(table)
            self.view_reset(self.col_type_list(table, self.cols_list()))

####################Delete Row functions####################

    def del_row(self, MainWindow):
        row = self.table.currentRow()
        self.table.removeRow(row)

####################From .ui --> .py transfer####################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB Manipulator"))
        self.open_db_btn.setText(_translate("MainWindow", "Open DB"))
        self.edit_db_btn.setText(_translate("MainWindow", "Edit Data"))
        self.close_db_btn.setText(_translate("MainWindow", "Close DB"))
        self.rename_col_btn.setText(_translate("MainWindow", "Rename Column"))
        self.del_col_btn.setText(_translate("MainWindow", "Delete Column"))
        self.del_row_btn.setText(_translate("MainWindow", "Delete Row"))
        self.text_type_rb.setText(_translate("MainWindow", "Text"))
        self.int_type_rb.setText(_translate("MainWindow", "Integer"))
        self.real_type_rb.setText(_translate("MainWindow", "Real"))
        self.create_table_btn.setText(_translate("MainWindow", "Create Table"))
        self.add_col_btn.setText(_translate("MainWindow", "Add Column"))
        self.or_info.setText(_translate("MainWindow", "--OR--"))
        self.blob_type_rb.setText(_translate("MainWindow", "Blob"))
        self.data_type_info.setText(_translate("MainWindow", "Data Types:"))
        self.show_table_btn.setText(_translate("MainWindow", "Show Data"))
        self.rename_table_btn.setText(_translate("MainWindow", "Rename Table"))
        self.exit_table_btn.setText(_translate("MainWindow", "Exit Table"))
        self.del_table_btn.setText(_translate("MainWindow", "Delete Table"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
