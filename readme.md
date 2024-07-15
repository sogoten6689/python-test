# install lib for python
pip install mysql-connector-python for python connect database
pip install Flask to start https service

# setup database mysql, create user and grant permission

# step run
## 1. run script to create database, table
create_database_script.sql

## 2. run python insert_data_search.py to generate data cho keyword search
python insert_data_search.py

## 3. run sql to register user subcription 
insert_user_subscription.sql

## 4. create python http app service for query data
app.py

## 5. run unit test to test app.py
unit_test.py


## summary

what i did: meet the requirements
    + get volume search keyword daily or hourly by group DATE
    + store keyword, keyword_volume, 
what i am not done: 
    + not create job to run daily at 9AM
    + unit test not cover all cases yet
