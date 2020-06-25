
#Author: Guilherme Santos
#Github: https://github.com/eguidos
#LinkedIn Profile: https://www.linkedin.com/in/guilherme-santos-754864108/


BASEFILE=$(pwd)
SPARK_SUBMIT=/usr/local/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit
MYSQL=$BASEFILE/mysql
APP=$BASEFILE/main

#This loop goes through every SQL file and executes its infrastrucure.


#The following command sets up python packages


export export PYTHONPATH=`pwd`

#So that, Spark execution collect all data needed, and then inserts into OLIST database tables.
$SPARK_SUBMIT $APP/app.py
