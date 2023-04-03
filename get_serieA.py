# streamlit_app.py

import streamlit as st
import snowflake.connector

my_db.connect(username=st.secrets.DB_USERNAME, password=st.secrets.DB_PASSWORD, account="xb47661.eu-west-2.aws",role="sysadmin",)

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from DEMO.STREAMLIT.SERIE_A_COMPLETE;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
