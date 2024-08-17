import pandas as pd
import matplotlib.pyplot as plt

# This line is needed to display plots inline within Jupyter Notebook
%matplotlib inline

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\sets.csv'
df = pd.read_csv(file_path)

# Group by year and count the number of sets
sets_by_year = df.groupby('year')['set_num'].count()

# Remove the last two years from the series
sets_by_year_trimmed = sets_by_year[:-2]
print(sets_by_year_trimmed)

# Plot the data as a line graph
plt.figure(figsize=(10, 6))
sets_by_year_trimmed.plot(kind='line', marker='o')
plt.title('Number of LEGO Sets Released Per Year (Excluding Last 2 Years)')
plt.xlabel('Year')
plt.ylabel('Number of Sets')
plt.grid(True)
plt.show()