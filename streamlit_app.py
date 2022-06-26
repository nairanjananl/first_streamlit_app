import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled, Free-Range Egg')
                
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's pick a pick list here so they can pick a fruit they want
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)
#Create the repeatable code block (adding a function)
def get_fruityvice_data(this_fruit_choice):
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information")
   else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
#New section to display api Fruityvice response
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information")
   else:
    back_from_function = get fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

#import requests
# normalize the data from json file
# put the normalized data in a table


#don't run any code past here while we troubleshoot
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("FRUIT_LOAD_LIST contains:")
streamlit.dataframe(my_data_rows)

#allow the end-user to add a fruit to the list
add_fruit_to_list = streamlit.text_input('What fruit would you like to add to the list?','jackfruit')

streamlit.write('Thanks for adding ', add_fruit_to_list, 'to the list')
