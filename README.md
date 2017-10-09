## Project Title
### Logs Analysis 
This is Logs Analysis project which builds an internal reporting tool holding an informative summary based on logs data. This gets connected to the database to fetch the information.

## Pre-Requisites
1. Download the project folder from given github repository location. 
2. To run this project you will need to install following :
    1) [python 3](https://www.python.org/downloads/)
    2) [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to install and manage the VM
   3) [Python3 Psycopg2 DB-API](http://initd.org/psycopg/docs/install.html)

## Installation 
1. Download the given project folder.
2. Install Vagrant and VirtualBox. This will give you the PostgreSQL database and support software needed for this project.
3. You can use Github to fork and clone the repository [here](https://github.com/udacity/fullstack-nanodegree-vm) for VM configuration. 
4. From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it.
5. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM!
6. Download and install [Python3 Psycopg2 DB-API](http://initd.org/psycopg/docs/install.html)
7. Run the python file viz. `queries.py` from the terminal to get the project results. 

## Code Example 
This project contains one python file viz. `queries.py`
1) It imports `pysocpg2` python DB-API 
2) There is a code to make a connection with the given database.
` conn = psycopg2.connect("dbname=news")`
3) It creates queries to fetch the information from connected database.
eg. `query1 = ("select a.title , count(l.path) from articles as a, log as l "....`
4) It uses `.format()` python functionality to format the output data.
eg. `print('{} - {} views'.format(row[0], row[1]))`
5) At the end it closes the connection made with the database.
`conn.close()`

## References 
1. [Python psycopg2 DB-API](http://initd.org/psycopg/docs/)
2. [Postgresql Documentation](https://www.postgresql.org/docs/9.0/static/index.html)
3. For formatting output data using - [.format in python](https://pyformat.info/)


