import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/Shoaib/Desktop/Code Sentinel Intern/country_wise_latest.csv")

print(df.info())

df_cal=df.select_dtypes(include=['number'])
df_data=df_cal.corr()
plt.figure(figsize=(12, 6))
axis_corr= sns.heatmap(df_data, vmin=-1, vmax=1, center=0, cmap='coolwarm',linewidths=.5, square=True)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.title("Correlation HEATMAP")
#plt.show()

Most_Frequent_Region=df.sort_values(by='Deaths',ascending=False)
print("\n\nMost 5 Frequent WHO Regions Countries Death Rate:\n ",Most_Frequent_Region['WHO Region'].value_counts().head(5))

Most_Frequent_Country=df.sort_values(by='Confirmed last week', ascending=False)
print("\n\nMost 5 Frequent Countries Confirmed Last Week:\n", Most_Frequent_Country[['Country/Region','Confirmed last week']].head(5))

plt.figure(figsize=(5,2))
plt.hist(df['Deaths'], bins=20, color='blue', edgecolor='white')
plt.xlabel("Number of Deaths")
plt.ylabel("Count")
plt.title("Histogram of Deaths")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.title('Distribution of Deaths (Boxplot)')
plt.ylabel('Deaths (by country)')
sns.boxplot(y='Deaths', data=df, color='Purple')
plt.tight_layout()
plt.savefig('deaths_boxplot.png')
plt.show()