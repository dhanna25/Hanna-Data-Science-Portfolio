import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will present us with data!")

# Initialize session state for DataFrame if not already initialized
if 'df' not in st.session_state:
    # Read data from CSV (this only happens once when app is first loaded)
    st.session_state.df = pd.read_csv("data/studyabroad_data.csv")

# Display the dataset
st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(st.session_state.df)

st.subheader("Average Ratings by City")

# Group data by city and calculate the mean rating
city_ratings = st.session_state.df.groupby("City")["Rating"].mean()

# Display the bar chart
st.bar_chart(city_ratings)

st.subheader("Tell us about your time abroad!")

# Dropdown for selecting city and rating
city = st.selectbox("Select a city", st.session_state.df["City"].unique())
rating = st.selectbox("Rate your time abroad", list(range(1, 11)))
st.write(f"You selected: {rating}")

if st.button("Submit Rating"):
    # Create a new row with the user input
    new_entry = pd.DataFrame({'Name': ['User'], 'City': [city], 'Rating': [rating]})
    
    # Append the new entry to the existing dataframe stored in session state
    st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)

    # Recalculate average ratings per city
    updated_city_ratings = st.session_state.df.groupby("City")["Rating"].mean()

    # Display updated chart
    st.subheader("Updated Ratings by City")
    st.bar_chart(updated_city_ratings)

    # Display the updated dataframe
    st.write("Here's the updated dataset:")
    st.dataframe(st.session_state.df)
