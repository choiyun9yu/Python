import os
import pandas as pd
from datetime import datetime, timedelta
import time
from sqlalchemy import create_engine
from flask import Flask, request, redirect, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import pymysql as ps

def con():
    conn = ps.connect(host='localhost', user='root', passwd='12345', db='aqu4men')
    return conn

def insert_db(table, calumns, values):
    conn = con()
    curs = conn.cursor()
    sql = f"insert into {table} {calumns} values {values};"
    curs.execute(sql)
    conn.commit()
    curs.close()
    conn.close()
    return sql

def select_db(calumn,table, where):
    conn = con()
    curs = conn.cursor()
    sql = f"selet {calumn} from {table} where {where} "
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    curs.close()
    conn.close()
    return sql