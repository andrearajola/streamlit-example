# streamlit_app.py

import streamlit as st
from snowflake.snowpark.session import Session

def create_session_object():
   connection_parameters = {
      "account": "xb47661.eu-west-2.aws",
      "user": "ARAJOLA",
      "password": st.secrets.DB_PASSWORD,
      "role": "SYSADMIN",
      "warehouse": "COMPUTE_WH",
      "database": "DEMO",
      "schema": "STREAMLIT"
   }
   session = Session.builder.configs(connection_parameters).create()
   return session

def run_query(query):
    with session.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from DEMO.STREAMLIT.SERIE_A_COMPLETE;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
