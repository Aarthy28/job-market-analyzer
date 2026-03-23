import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/jobs.csv")

# Clean column names (removes extra spaces)
data.columns = data.columns.str.strip()

# Show basic info (for checking)
print(data.head())
print(data.columns)

# -------------------------------
# 📊 1. Job Title Analysis
# -------------------------------
job_counts = data['Job Title'].value_counts().head(10)

plt.figure()
job_counts.plot(kind='barh', figsize=(10,5))

plt.title("Top 10 Most Common Job Roles")
plt.xlabel("Number of Jobs")
plt.ylabel("Job Title")

plt.tight_layout()
plt.savefig("top_jobs.png")
plt.show()


# -------------------------------
# 🌍 2. Location Analysis
# -------------------------------
location_counts = data['Location'].value_counts().head(10)

plt.figure()
location_counts.plot(kind='barh', figsize=(10,5))

plt.title("Top 10 Job Locations")
plt.xlabel("Number of Jobs")
plt.ylabel("Location")

plt.tight_layout()
plt.savefig("top_locations.png")
plt.show()


# -------------------------------
# 🏢 3. Company Analysis
# -------------------------------
company_counts = data['Company Name'].value_counts().head(10)

plt.figure()
company_counts.plot(kind='barh', figsize=(10,5))

plt.title("Top Hiring Companies")
plt.xlabel("Number of Jobs")
plt.ylabel("Company")

plt.tight_layout()
plt.savefig("top_companies.png")
plt.show()


# -------------------------------
# 💰 4. Salary Distribution
# -------------------------------
# (only works if salary is numeric)

if data['Salary'].dtype != 'object':
    plt.figure()
    data['Salary'].plot(kind='hist', bins=20, figsize=(8,5))

    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("salary_distribution.png")
    plt.show()
else:
    print("Salary column is not numeric, skipping salary analysis.")