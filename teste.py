import pandas as pd
import sqlite3

df = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_ind_2010.csv", encoding='latin1', sep=';')

print(df)