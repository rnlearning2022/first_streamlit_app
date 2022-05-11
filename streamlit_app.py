import streamlit
import pandas

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Menu Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Sprinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick son fruits:", list(myfruit_list.index))
#Display the table on the page
streamlit.dataframe(my_fruit_list)
