import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will present us with !")

df = pd.DataFrame({
    'Name': ['Andrea', 'Avery', 'Jordan', 'Alfonso', 'Mia', 'Jack', 'Mauro', 'Miguel', 'Miranda','Jonny'],
    'City': ['London', 'Sydney', 'London', 'Toledo', 'Dublin', 'Rome', 'Sydney', 'Sydney', 'Madrid', 'Toledo'],
    'Rating': [7,10,8,6,9,8,10,9,7,8]
})
st.write("Here's a simple table:")
st.dataframe(df)

st.subheader("Average Ratings by City")

# Group data by city and calculate the mean rating
city_ratings = df.groupby("City")["Rating"].mean()

# Display the bar chart
st.bar_chart(city_ratings)

st.subheader("Tell us about your time abroad!")

# Dropdown for selecting city and rating
city = st.selectbox("Select a city", df["City"].unique())
rating = st.selectbox("Rate your time abroad", list(range(1, 11)))
st.write(f"You selected: {rating}")

if st.button("Submit Rating"):
    # Create a new row with the user input
    new_entry = pd.DataFrame({'Name': ['User'], 'City': [city], 'Rating': [rating]})
    
    # Append the new entry to the existing dataframe
    df = pd.concat([df, new_entry], ignore_index=True)

    # Recalculate average ratings per city
    updated_city_ratings = df.groupby("City")["Rating"].mean()

    # Display updated chart
    st.subheader("Updated Ratings by City")
    st.bar_chart(updated_city_ratings)
