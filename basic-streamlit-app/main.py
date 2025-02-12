'''import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will present us with data!")

# Read data from CSV
df = pd.read_csv("data/studyabroad_data.csv")
st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(df)

# Initialize session state for DataFrame if not already initialized
if 'df' not in st.session_state:
    st.session_state.df = df

st.subheader("Average Ratings by City")

# Group data by city and calculate the mean rating
city_ratings = st.session_state.df.groupby("City")["Rating"].mean()

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
    st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)

    # Recalculate average ratings per city
    updated_city_ratings = st.session_state.df.groupby("City")["Rating"].mean()

    # Display updated chart
    st.subheader("Updated Ratings by City")
    st.bar_chart(updated_city_ratings)
>>>>>>> Stashed changes

    # Display the updated dataframe
    st.write("Here's the updated dataset:")
    st.dataframe(st.session_state.df)'''

'''import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will present us with data!")

# Initialize session state for DataFrame if not already initialized
if 'df' not in st.session_state:
    # Read data from CSV (this only happens once when app is first loaded)
    st.session_state.df = pd.read_csv("data/studyabroad_data.csv")
    st.session_state.df  # Save to session state

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
    st.dataframe(st.session_state.df)'''

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


df = load_data(csv_file)


st.write("Here's the data table:")
st.dataframe(df)


st.subheader("Average Ratings by City")


# Group data by city and calculate the mean rating
city_ratings = df.groupby("City")["Rating"].mean()


# Display the bar chart
st.bar_chart(city_ratings)


st.subheader("Tell us about your time abroad!")


# Dropdown for selecting city and rating
if not df.empty:
   city = st.selectbox("Select a city", df["City"].unique())
   rating = st.selectbox("Rate your time abroad", list(range(1, 11)))
   st.write(f"You selected: {rating}")


   if st.button("Submit Rating"):
       # Create a new row with the user input
       new_entry = pd.DataFrame({'Name': ['User'], 'City': [city], 'Rating': [rating]})
      
       # Append the new entry to the existing dataframe
       df = pd.concat([df, new_entry], ignore_index=True)
      
       # Save updated data back to CSV
       df.to_csv(csv_file, index=False)
      
       # Recalculate average ratings per city
       updated_city_ratings = df.groupby("City")["Rating"].mean()
      
       # Display updated chart
       st.subheader("Updated Ratings by City")
       st.bar_chart(updated_city_ratings)



