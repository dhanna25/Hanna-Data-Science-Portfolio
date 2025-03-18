# TidyData-Project
 The goal of this project is to demonstrate the ability to employ tidy data principles to disorganized data sets in order to make them more clear, comprehensible, and interpretable. Tidy data principles, as presented to us in our readings and in class revolve around consistency, efficiency, and easy analysis. As asked of us in the assignment the main principles include 1) putting each variable in its own column, which has been done by placing the variables such as "medalist_name", "sport", "gender", and "medal" into separate columns. The second principle applied in this project is that each observation forms a row. For example, in this case, each row should present a medalist and their associated attributes. Additionally, each observational unit should form its own table. This has been demonstrated by placing medalists, sports, and medals, into their own tables. 

 # Instructions
 1) To run the Notebook, ensure than you download the jupiter notebook as well as the prospective dataset (olympics_08_medalists (1).csv).
 2) Open the notebook in a compatible environment.
 3) Run the notebook and examine the output cells as well as the visualizations. 
Dependencies and their purpose:
pandas: data manipulation and analysis
matplotlib: static visualizations

# Pre-Processing Steps:
Using pd.melt(), we reshape the dataset from wide to long and split the sport_gender column into separate columns. Using dropna, we remove any missing values in the medal column. Using factorize(), a unique medalist_id is generated for each medalist to summarize medal counts for the pivot table. 

# References
1) Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
2) Tidy Data Paper: https://vita.had.co.nz/papers/tidy-data.pdf




![alt text](<Screenshot 2025-03-17 at 8.53.51 PM.png>)

![alt text](<Screenshot 2025-03-17 at 8.54.35 PM.png>)