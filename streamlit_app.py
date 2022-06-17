#placeholder
import streamlit
import pandas
import snowflake.connector

streamlit.title('My Parents New Healthy Diner');
streamlit.header('Breakfast menu');
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit');

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'] )

#streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'] )

fruit_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_to_show)
#-----
streamlit.text('1')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
streamlit.text('2')
my_cur = my_cnx.cursor()
streamlit.text('3')
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
streamlit.text('4')
my_data_row = my_cur.fetchone()
streamlit.text('5')
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
