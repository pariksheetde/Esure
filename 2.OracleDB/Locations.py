#!/usr/bin/env python3
# Copyright 2022 Pariksheet DE
# db-query.py as of 2021-04-07
# runs on Python 3.8.0

import cx_Oracle

def main():
    db = cx_Oracle.connect("HR/HRS@localhost:1521/XE")
    cur = db.cursor()
    qry_locs = """SELECT 
                    l.location_id, 
                    l.location_name
                    FROM 
                    locations l order by 1 asc"""
    cur.execute(qry_locs)
    row = cur.fetchall()
    print(row)

    print(f"Record(s) returned: {cur.rowcount}")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()