"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  : IT
Date  : 12/23/2026

"""

# ====================================================================== CLASS
class Record:                                                                 # a record class to group data all together
    over_limit_count = 0                                                      # a class variable to check how many servers are over limit 

    def __init__(self, label, value, limit):
        self.label = label                                                    # holds the label for this object instance
        self.value = value                                                    # holds the value for this object instance
        self.limit = limit                                                    # holds the limit for this object instance

        if self.status() == "OVER LIMIT":                                     # calls the status function to see if its over limit or not then it adds 1
            Record.over_limit_count += 1

    def percent(self):
        percentage = (self.value/self.limit) * 100
        return percentage
    
    def status(self):
        """Return the status after calculating the percentage"""
        p = self.percent()                                                    # percent result is stored in p variable
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== New text file

with open("Records.txt" , "w")as f:
    f.write ("R-111,158,158\n")
    f.write ("R-112,1280,1000\n")
    f.write ("R-113,787,345\n")
    f.write ("R-114,451,454\n")
    f.write ("R-115,725,625\n")
    f.write ("R-116,1999,6248")

# ==================================================================== RECORDS
def load_records(path):                                                       # to define a function to read the saved data file and load it back to the program       
    records = []                                                              # to make an empty list that will hold all the objects together
    with open (path)as f:                                                     # to open data file in read only mode
        for line in f:                                                        # to loop the text file line by line
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))         # to create an new record with dat aand add it to the list
    return records
result = load_records("Records.txt")                                          # to call function to load up all data from file and save list to variable

# ==================================================================== OUTPUT
for record in result:                                                         # to loop through each individual object saved in list to display the data
    print()
    print("=" * 34)
    print(f"     RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Label:             {record.label}")
    print(f"Value:             {record.value}")
    print(f"Limit:             {record.limit}")
    print(f"Status:            {record.status()}")
    print("=" * 34)
    print(f"Total records that are OVER LIMIT: {Record.over_limit_count}")    # summary 
    print("=" * 34)
    print("=" * 34)
