import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled, Free-Range Egg')
                
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's pick a pick list here so they can pick a fruit they want
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)
