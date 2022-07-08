import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('Data Upload Demo')

streamlit.header('Pulling Data From Snowflake')

streamlit.text("Fruit load list contains:")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
      return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

streamlit.header('Putting Data Into Snowflake')

def insert_row_snowflake(new_row):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + new_row + "')")
      return "Thanks for adding " + new_row
   
add_row = streamlit.text_input('Record name here: ')
if streamlit.button('Add to Table'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_row)
   my_cnx.close()
   streamlit.text(back_from_function)
