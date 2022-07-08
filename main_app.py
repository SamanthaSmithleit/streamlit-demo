import streamlit
import snowflake.connector

streamlit.title('Data Upload Demo')

streamlit.header('Pulling Data From Snowflake')

streamlit.header("Fruit load list contains:")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
      return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)
