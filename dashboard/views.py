from django.shortcuts import render

# Create your views here.

#########TESTING pnadas e sqlite
import pandas as pd
import sqlite3

con = sqlite3.connect("./db.sqlite3")

df = pd.read_sql_query("SELECT * from relatorios_tableactionmodel", con)

print(df)