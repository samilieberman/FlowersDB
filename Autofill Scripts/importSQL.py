import csv
import sqlite3
from datetime import datetime
from datetime import timedelta
import os
import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # try:
    conn = sqlite3.connect(db_file)
    return conn
    # except Error as e:
    #     print(e)

    # return None


def create_sightings(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = "INSERT INTO SIGHTINGS(NAME, PERSON, LOCATION, SIGHTED) VALUES(?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_features(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = "INSERT INTO FEATURES(LOCATION, CLASS, LATITUDE, LONGITUDE,MAP,ELEV) VALUES(?, ?, ?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_flowers(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = "INSERT INTO FLOWERS(GENUS, SPECIES, COMNAME) VALUES(?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


dir = os.getcwd()
database = dir + '\\..\\mysite\\db.sqlite3'

choice = ""
choice = raw_input("Please type which file you'd like to import: ")

if choice.lower() == 'sightings':
    filename = 'SIGHTINGS.csv'
    with open(filename) as csv_file:
        conn = create_connection(database)
        with conn:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('Column names are ', row)
                    line_count += 1
                else:
                    parts = row[4].split('/')
                    for i in range(0, 2):
                        if len(parts[i]) == 1:
                            parts[i] = '0' + parts[i]
                    new_date = parts[2] + '-' + parts[0] + '-' + parts[1]
                    print(new_date)
                    flower = (str(row[1]), str(row[2]), str(row[3]), new_date)
                    flower_id = create_sightings(conn, flower)
                    line_count += 1
            print('Processed', line_count, ' lines.')
elif choice.lower() == 'flowers':
    filename = 'FLOWERS.csv'
    with open(filename) as csv_file:
        conn = create_connection(database)
        with conn:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('Column names are ', row)
                    line_count += 1
                else:
                    flower = (str(row[1]), str(row[2]), str(row[3]))
                    flower_id = create_flowers(conn, flower)
                    line_count += 1
elif choice.lower() == 'features':
    filename = 'FEATURES.csv'
    with open(filename) as csv_file:
        conn = create_connection(database)
        with conn:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('Column names are ', row)
                    line_count += 1
                else:
                    flower = (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]))
                    flower_id = create_features(conn, flower)
                    line_count += 1
            print('Processed', line_count, ' lines.')

# create a database connection
# conn = create_connection(database)
# with conn:
#     # create a new project
#     flower = ('TEST', 'FLOWER', 'test_flower')
#     flower_id = create_flowers(conn, flower)

    # tasks
    # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
    # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

    # # create tasks
    # create_task(conn, task_1)
    # create_task(conn, task_2)
