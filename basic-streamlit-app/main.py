<<<<<<< Updated upstream
<<<<<<< Updated upstream


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
=======
''''''# testing push
>>>>>>> Stashed changes
=======
''''''# testing push
>>>>>>> Stashed changes
import streamlit as st
import pandas as pd

st.title("Study Abroad Data")
st.subheader("This app will tell us how students rate their study abroad experiences!")

<<<<<<< Updated upstream
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
=======
#df = pd.read_csv("data/study_abroad_data.csv")
#st.write("Here's the dataset loaded from a CSV file:")
#st.dataframe(df)

#df = pd.read_csv("data/study_abroad_data.csv")
#st.write("Here's the dataset loaded from a CSV file:")
#st.dataframe(df)

df = pd.DataFrame({
   'Name': ['Andrea', 'Avery', 'Jordan', 'Alfonso', 'Mia', 'Jack', 'Mauro', 'Miguel', 'Miranda','Jonny'],
   'City': ['London', 'Sydney', 'London', 'Toledo', 'Dublin', 'Rome', 'Sydney', 'Sydney', 'Madrid', 'Toledo'],
   'Rating': [7,10,8,6,9,8,10,9,7,8]
})
st.write("Here's a simple table:")
>>>>>>> Stashed changes
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
    
<<<<<<< Updated upstream
      df = pd.concat([df, new_entry], ignore_index=True)
      df.to_csv(csv_file, index=False)
    
      updated_city_ratings = df.groupby("City")["Rating"].mean()
    
      st.subheader("Updated Ratings by City")
      st.bar_chart(updated_city_ratings)
=======
    # Append the new entry to the existing dataframe
    df = pd.concat([df, new_entry], ignore_index=True)

    # Recalculate average ratings per city
    updated_city_ratings = df.groupby("City")["Rating"].mean()

    # Display updated chart
    st.subheader("Updated Ratings by City")
    st.bar_chart(updated_city_ratings)
''''''
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
<<<<<<< Updated upstream
=======
''''''
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
    st.dataframe(st.session_state.df)
<<<<<<< Updated upstream
'''
>>>>>>> Stashed changes
=======
'''
>>>>>>> Stashed changes
