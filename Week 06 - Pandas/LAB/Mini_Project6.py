"""
RECORD CHECK  -  my version
===========================

Name  : ROHITHA BIJU KRISHNAN
Lane  : IT
Date  : 8/11/2026 

"""
# ==================================================================== LOAD

import pandas as pd
df = pd.read_csv("server_records.csv")                    # to read the data file 

# ================================================================= PROCESS

df["Percent"] = ((df["value"] / df["limit"]) * 100).round(1)
# to create a status column to assign status based on the percent value using a lambda function
df["Status"] = df["Percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")

# ================================================================== OUTPUT

import matplotlib.pyplot as plt

print("Rows that do not have OK status:")                 # to count the rows that do not have status 'OK'
print(df[df["Status"] != "OK"])

print("\n\n")

print("Count per group:")                                 # to plot the counts of each status
status_counts = df.groupby("Status")["Percent"].count()   # use groupby to count the number of records in each status group
print(status_counts)

df.to_csv("server_records_report.csv", index=False)       # to save full data frame to a new csv file

status_counts.plot(kind= "bar")                           # create bar chart by using calculated status counts
plt.title("Count of Records by Status")                   # give title to the top of the bar graph
plt.tight_layout()                                        # to atomatically adjust the spacing before saving
plt.savefig("server_records_counts.png")                  # saves chart as real image file 
plt.show()

# ==========================================================================