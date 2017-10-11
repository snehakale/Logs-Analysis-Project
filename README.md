## Project Title
### Logs Analysis 
This is Logs Analysis project which builds an internal reporting tool holding an informative summary based on logs data. This gets connected to the database to fetch the information.

## Pre-Requisites
1. Download the project folder from given github repository location. 
2. To run this project you will need to install following :
    1) [python 3](https://www.python.org/downloads/)
    2) [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to install and manage the VM
   3) [Python3 Psycopg2 DB-API](http://initd.org/psycopg/docs/install.html)
    4) [Download the folder](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) for the database operations.

## Installation 
1. Download the given project folder.
2. Install Vagrant and VirtualBox. 
This will give you the PostgreSQL database and support software needed for this project.
3. You can use Github to fork and clone the repository [here](https://github.com/udacity/fullstack-nanodegree-vm) for VM configuration. 
4. From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it.
5. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM!
6. Unzip the downloaded database folder. There is a file inside called as `newsdata.sql`. Put this file into the vagrant directory, which is shared with your virtual machine. To load the data, cd into the **vagrant** directory and use the command 
`psql -d news -f newsdata.sql`.
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
7. Download and install [Python3 Psycopg2 DB-API](http://initd.org/psycopg/docs/install.html)
8. From the downloaded project folder, get the python file `queries.py` and place it in **vagrant** directory,which is shared with your virtual machine. cd into **vagrant** directory and run the python file viz. `queries.py` from the terminal.
eg. `vagrant@vagrant:/vagrant$ python queries.py`


## Code Example 
This project contains one python file viz. `queries.py`
1) It has shebang line which provides the version of python required for the interpreter.
`#! /usr/bin/env python3`
1) It imports `pysocpg2` python DB-API 
2) Function `db_connect(...)` creates a connection with the given database and returns the connected database object and cursor for it.
`db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor`
3) Function `get_result(..)` will execute the queries written inside it
eg. `query1 = ("select a.title , count(l.path) from articles as a,...`
 and uses  `.format()` python functionality to format the output data.
eg. `print ('{} - {} views'.format(row[0], row[1]))`
 At the end it closes the connection made with the database.
`db.close()`

## References 
1. [Python psycopg2 DB-API](http://initd.org/psycopg/docs/)
2. [Postgresql Documentation](https://www.postgresql.org/docs/9.0/static/index.html)
3. For formatting output data using - [.format in python](https://pyformat.info/)


