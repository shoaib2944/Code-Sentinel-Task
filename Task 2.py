import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("C:/Users/Shoaib/Desktop/Code Sentinel Intern/titanic.csv")
print(df.columns, "\n\n")
print("PassengerID Null: ", df.PassengerId.isnull().sum())
print("Survived Null: ",df['Survived'].isnull().sum())
print("Pclass Null", df['Pclass'].isnull().sum())
print("Name Null: ", df['Name'].isnull().sum())
print("Sex Null: ", df['Sex'].isnull().sum())
print("Age Null: ", df['Age'].isnull().sum())
u=df[['Name','Age']]
print(u)
median=df['Age'].median()
df.fillna({'Age': median}, inplace=True)
print("Age Null After Fillna Operation: ", df['Age'].isnull().sum())
print("SibSp Null: ",df['SibSp'].isnull().sum())
print("Parch Null: ",df['Parch'].isnull().sum())
print("Ticket Null: ",df['Ticket'].isnull().sum())
print("Embarked Null: ",df['Embarked'].isnull().sum())
print("Fair Null: ",df.Fare.isnull().sum())
mod=df.Fare.mode()[0]
df.fillna({'Fare':mod}, inplace=True)
print("Fair Null After Fillna Operation: ",df.Fare.isnull().sum())
print("Cabin Null: ",df['Cabin'].isnull().sum())
df.dropna(subset=['Cabin'],inplace=True)
print("Cabin Null after Dropna Operation: ",df['Cabin'].isnull().sum())

print("/n/n/n/n/n/n")

print("PassengerID Duplicate: ", df.PassengerId.duplicated().sum())
print("Survived duplicated: ",df['Survived'].duplicated().sum())
print("Pclass duplicated", df['Pclass'].duplicated().sum())
print("Name duplicated: ", df['Name'].str.title().replace(r'[^A-Za-z\s]','',regex=True).duplicated().sum())
print("Sex duplicated: ", df['Sex'].duplicated().sum())
df['Sex']=df['Sex'].str.title().replace(r'[^A-Za-z\s]','',regex=True)
print(df.Sex)
print("Age duplicated: ", df['Age'].duplicated().sum())
print("SibSp duplicated: ",df['SibSp'].duplicated().sum())
print("Parch duplicated: ",df['Parch'].duplicated().sum())
print("Ticket duplicated: ",df['Ticket'].duplicated().sum())
print("\n\n\n\n\n", df['Ticket'].unique(), "\n\n\n\n\n")
df.drop_duplicates(subset=['Ticket'],inplace=True)
print("After Dropping Ticket duplicates: ",df['Ticket'].duplicated().sum())

print("Embarked Null: ",df['Embarked'].isnull().sum())
print("Fair Null: ",df.Fare.isnull().sum())
mod=df.Fare.mode()[0]
df.fillna({'Fare':mod}, inplace=True)
print("Fair Null After Fillna Operation: ",df.Fare.isnull().sum())
print("Cabin Null: ",df['Cabin'].isnull().sum())
df.dropna(subset=['Cabin'],inplace=True)
print("Cabin Null after Dropna Operation: ",df['Cabin'].isnull().sum())

survival_rate_by_sex = df.groupby('Sex')['Survived'].mean()

# 3. Create the Bar Chart
# The names of the bars ('male', 'female') come from the 'Sex' column
x_values = survival_rate_by_sex.index

# The height of the bars (the survival rates) come from our calculation
y_values = survival_rate_by_sex.values

# 'plt.bar' creates the bar chart
plt.bar(x_values, y_values, color=['salmon', 'skyblue'])

# 4. Add labels and a title
plt.title("Titanic Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

# Make sure the y-axis goes from 0 to 1 for a clear view of the rates
plt.ylim(0, 1)

# 5. Show the chart
plt.show()