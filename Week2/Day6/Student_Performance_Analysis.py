# Dataset
# Name	   Math 	 Physics	   English
# Ali	   80	        75	        90
# Ahmed	   85	        95	        88
# Umar	   78	        82	        86

# Find:
    # Average marks
    # Highest marks
    # Lowest marks

# Add:
    # Average Marks
    # Total Marks
    # Grade

# Filter:
# Students having average marks greater than 85.

# Bonus
# Save modified data into a new CSV file.
# to_csv()

import pandas as pd

Students={
    "Name" : ["Ali", "Ahmed", "Umar"],
    "Math" : [80, 85, 78],
    "Physics" : [75, 95, 82],
    "English" : [90, 88, 86]
}

df=pd.DataFrame(Students)

# Average Marks
print("\nAverage Marks:")
print(f"The Average Marks of Math is: {df["Math"].mean()}")
print(f"The Average Marks of Physics is: {df["Physics"].mean()}")
print(f"The Average Marks of English is: {df["English"].mean()}")

# Highest Marks
print("\nHighest Marks")
print(f"The Highest Marks in Math is: {df["Math"].max()}")
print(f"The Highest Marks in Physics is: {df["Physics"].max()}")
print(f"The Highest Marks in English is: {df["English"].max()}")

# Lowest Marks
print("\nLowest Marks")
print(f"The Lowest Marks in Math is: {df["Math"].min()}")
print(f"The Lowest Marks in Physics is: {df["Physics"].min()}")
print(f"The Lowest Marks in English is: {df["English"].min()}")

# Add Total Marks
df["Total Marks"] = df[["Math", "Physics", "English"]].sum(axis=1)

# Add Average Marks
df["Average Marks"] = df["Total Marks"] / 3

# Add Grade
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average Marks"].apply(grade)

# Display Modified DataFrame
print("\nModified DataFrame:")
print(df)

# Students having average marks greater than 85.
Filter_df=df[df["Average Marks"] > 85]
print("\n",Filter_df)

df.to_csv("Students_Report.csv", index=False)
print("\nCSV file saved successfully as 'Students_Report.csv'")
