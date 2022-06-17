#placeholder
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


def get_fruityvice_data(this_fruit_choice):
    fruityadvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityadvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding: " + new_fruit


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
try:
    fruit_choice = streamlit.text_input('What fruit to add?')
    if not fruit_choice:
        streamlit.error('Provide informatin')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
    
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

add_my_fruit1 = streamlit.text_input('What fruit to add?')
if streamlit.button('Add Fruit to a List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit1)
    streamlit.dataframe(back_from_function)
    
    
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#streamlit.text('The fruit load list contains:')

#streamlit.text(fruits_selected)
#add_my_fruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[] )

#streamlit.stop()
