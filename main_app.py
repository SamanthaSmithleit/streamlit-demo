import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.set_page_config(page_title="Data Uploading", page_icon="❄️", layout="centered")

streamlit.title("Data Uploading ❄️")

streamlit.header('Pulling Data From Snowflake')

streamlit.text("Table contains:")
def get_table_contents():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * FROM TEST_TABLE")
      return my_cur.fetchall()

if streamlit.button('Get Table Contents'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_table_contents()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

streamlit.header('Putting Data Into Snowflake')

def insert_row_snowflake(new_row):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("INSERT INTO TEST_TABLE VALUES ('" + new_row + "')")
      streamlit.balloons()
      return "Thanks for adding " + new_row
   
add_row = streamlit.text_input('Record name here: ')
if streamlit.button('Add to Table'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_row)
   my_cnx.close()
   streamlit.text(back_from_function)
   
streamlit.header('Deleting Data')
def clear_table_contents():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("Truncate table TEST_TABLE")
      return "Table Cleared"

if streamlit.button('Clear Table Contents'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = clear_table_contents()
   my_cnx.close()
   streamlit.dataframe(back_from_function)
