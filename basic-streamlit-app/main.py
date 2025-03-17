

'''import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will tell us how students rate their study abroad experiences!")

csv_file = "studyabroad_data.csv"

def load_data(file):
  try:
      df = pd.read_csv(file)
      return df
  except FileNotFoundError:
      st.error("CSV file not found. Please make sure 'studyabroad_data.csv' is available.")
      return pd.DataFrame(columns=['Name', 'City', 'Rating'])
 
df = load_data(csv_file)

st.write("Here's the data table:")
st.dataframe(df)
st.subheader("Average Ratings by City")

city_ratings = df.groupby("City")["Rating"].mean()

st.bar_chart(city_ratings)
st.subheader("Tell us about your time abroad!")

if not df.empty:
  name = st.text_input("Enter your name", placeholder="Your Name")
  city = st.selectbox("Select a city", df["City"].unique())
  rating = st.selectbox("Rate your time abroad", list(range(1, 11)))
  st.write(f"You selected: {rating}")

  if st.button("Submit Rating"):
      new_entry = pd.DataFrame({'Name': ['User'], 'City': [city], 'Rating': [rating]})
    
      df = pd.concat([df, new_entry], ignore_index=True)
      df.to_csv(csv_file, index=False)
    
      updated_city_ratings = df.groupby("City")["Rating"].mean()
    
      st.subheader("Updated Ratings by City")
      st.bar_chart(updated_city_ratings)

'''
import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will tell us how students rate their study abroad experiences!")

csv_file = "studyabroad_data.csv"

def load_data(file):
  try:
      df = pd.read_csv(file)
      return df
  except FileNotFoundError:
      st.error("CSV file not found. Please make sure 'studyabroad_data.csv' is available.")
      return pd.DataFrame(columns=['Name', 'City', 'Rating'])
 
df=load_data(csv_file)

st.write("Here's the data table:")
st.dataframe(df)
st.subheader("Average Ratings by City")

city_ratings = df.groupby("City")["Rating"].mean()

st.bar_chart(city_ratings)
st.subheader("Tell us about your time abroad!")

if not df.empty:
  name = st.text_input("Enter your name", placeholder="Your Name")
  city = st.selectbox("Select a city", df["City"].unique())
  rating = st.selectbox("Rate your time abroad", list(range(1, 11)))
  st.write(f"You selected: {rating}")

  if st.button("Submit Rating"):
      new_entry = pd.DataFrame({'Name': ['User'], 'City': [city], 'Rating': [rating]})
    
      df = pd.concat([df, new_entry], ignore_index=True)
      df.to_csv(csv_file, index=False)
    
      updated_city_ratings = df.groupby("City")["Rating"].mean()
    
      st.subheader("Updated Ratings by City")
      st.bar_chart(updated_city_ratings)