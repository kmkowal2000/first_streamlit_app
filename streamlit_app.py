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

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'] )
fruit_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_to_show)

streamlit.header('Fruityvice fruit advice!')
fruit_choice = streamlit.text_input('What fruit to add?')
streamlit.write('The user has entered', fruit_choice)


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.text('The fruit load list contains:')
#streamlit.dataframe(my_data_row)
#streamlit.text(fruits_selected)
#add_my_fruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[] )

