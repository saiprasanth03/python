import pandas as pd
data = {
	"ID" : list(range(1,11)),
	"Name" : ["A","B","C","D","E","F","G","H","I","J"],
	"Age" : [20,19,19,20,18,22,20,20,18,19],
	"Marks" : [89,90,92,93,90,83,89,88,91,84],
	"City" : ["Jaipur","Delhi","Banglore","Mumbai","Tuni","Lucknow","Pune","Viskhapatnam","Kolkata","Chennai"]
}

df = pd.DataFrame(data)
print("First 5 rows using head()\n",df.head())
print("\nSingle column (Name)\n",df["Name"])
print("\nMultiple columns (Name ,Age)\n", df[["Name", "Age"]])
print("\nSingle row (index 2)\n",df.iloc[2])
print("\nRange of rows (index 4 to 8)\n",df.iloc[4:9])
