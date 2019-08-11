# DB-Manipulator
A desktop app to browse, edit, and customize your SQLite databases

<h1>Technologies:</h1>
Python 3
- PyQt5
- SQlite3
- CSV
- Pandas

<h1>Step 1</h1>

Choose a database file by clicking the "Open DB" button.

![db_1](https://user-images.githubusercontent.com/46886041/58078492-11e74680-7bd9-11e9-8295-412240d128d2.PNG)

<h1>Step 2</h1>

All of the SQLite tables from your selected database file will appear in the list display. In this mode, you can: rename any table with no alterations to data within the table, delete any table, and create tables and add them to your current database file.

If you want to change database files, click the "Close DB" button and repeat Step 1. If you want to view and edit information within a table, click the "Show Data" button.

![db](https://user-images.githubusercontent.com/46886041/58078499-17dd2780-7bd9-11e9-93bb-9d7fdc3ea5df.PNG)

<h1>Step 3</h1>

All of the data from your selected table will appear in the table display, while all of your column information will appear in the list display. In this mode, you can: edit and replace data in your table via table display, rename columns with no alterations to data in the column, delete any column, and add columns to your current table.

To save changes made in the table display, click the "Edit Data" button. To view in the table display changes you made to columns in the list display, click the "Refresh" button. If you want to change to a different table in your current database file, click the "Exit Table" button and select a new table.

![db_2](https://user-images.githubusercontent.com/46886041/58078517-24618000-7bd9-11e9-8f09-fdf70f5f7195.PNG)

Lastly, the transfer.csv file is necessary only to transfer editted data from the table display to a replica SQLite table--no other information from the selected table is altered in any way. It's also necessary to mention that this app is essentially a simplified version of the DB Browser desktop app.



