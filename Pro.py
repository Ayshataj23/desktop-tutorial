import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 1. LOAD DATASET
# ============================================
df = pd.read_csv("StudentsPerformance.csv")

# ============================================
# 2. INSPECT DATA
# ============================================
print("First 10 rows:")
print(df.head(10))

print("\nShape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData info:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

# ============================================
# 3. DATA CLEANING
# ============================================
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Rename columns
df.columns = ['gender', 'race', 'parent_edu', 'lunch',
               'test_prep', 'math', 'reading', 'writing']

# ============================================
# 4. STATISTICAL ANALYSIS
# ============================================
print("\nAverage math score:", df['math'].mean())
print("Highest math score:", df['math'].max())
print("Lowest math score:", df['math'].min())

print("\nAverage scores by gender:")
print(df.groupby('gender')[['math', 'reading', 'writing']].mean())

print("\nAverage scores by test preparation:")
print(df.groupby('test_prep')[['math', 'reading', 'writing']].mean())

# ============================================
# 5. FILTERING
# ============================================
high_scorers = df[df['math'] >= 80]
print("\nHigh scorers (math >= 80):", len(high_scorers))

female_high = df[(df['gender'] == 'female') & (df['math'] >= 80)]
print("Female high scorers:", len(female_high))

# ============================================
# 6. SORTING - Top 10 students
# ============================================
top_10 = df.sort_values(by='math', ascending=False).head(10)
print("\nTop 10 students by math score:")
print(top_10[['gender', 'math', 'reading', 'writing']])

# ============================================
# 7. NEW COLUMNS - Pass/Fail and Grade
# ============================================
df['average'] = (df['math'] + df['reading'] + df['writing']) / 3

df['result'] = df['average'].apply(
    lambda x: 'Pass' if x >= 50 else 'Fail'
)

def assign_grade(avg):
    if avg >= 85: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    elif avg >= 50: return 'D'
    else: return 'F'

df['grade'] = df['average'].apply(assign_grade)

print("\nPass/Fail count:")
print(df['result'].value_counts())

print("\nGrade distribution:")
print(df['grade'].value_counts())

# ============================================
# 8. VISUALIZATIONS
# ============================================

# Graph 1: Average scores by gender
gender_avg = df.groupby('gender')[['math', 'reading', 'writing']].mean()
gender_avg.plot(kind='bar')
plt.title('Average Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('graph1_gender.png')
plt.show()

# Graph 2: Math score distribution
plt.figure()
plt.hist(df['math'], bins=20, edgecolor='black')
plt.title('Math Score Distribution')
plt.xlabel('Math Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('graph2_math_hist.png')
plt.show()

# Graph 3: Test preparation impact
prep_avg = df.groupby('test_prep')[['math', 'reading', 'writing']].mean()
prep_avg.plot(kind='bar')
plt.title('Impact of Test Preparation on Scores')
plt.xlabel('Test Preparation')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('graph3_testprep.png')
plt.show()

# Graph 4: Grade distribution
plt.figure()
df['grade'].value_counts().plot(kind='bar', edgecolor='black')
plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('graph4_grades.png')
plt.show()

# Graph 5: Pass/Fail pie chart
plt.figure()
df['result'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pass vs Fail')
plt.ylabel('')
plt.tight_layout()
plt.savefig('graph5_passfail.png')
plt.show()

# ============================================
# 9. EXPORT TO EXCEL
# ============================================
df.to_excel('Cleaned_Student_Data.xlsx', index=False)
print("\nFile saved as Cleaned_Student_Data.xlsx")

print("\nProject Complete!")
