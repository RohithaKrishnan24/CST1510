"""
RECORD CHECK  -  my version
===========================

Name  :  Rohitha Biju Krishnan
Lane  :  IT
Date  :  11/14/2026

"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy line into a dictionary"""
    line = [l.strip() for l in raw_line.strip().split(",")]            # to remove outer spaces, split at commas, seperate each piece

    hostname = line[0].upper()                                         # hostname piece is converted to uppercase
    used = int(line[1].split("=")[1].strip())                          # used piece splits at "=" and stores the number after it and converted to integer
    total = int(line[2].split("=")[1].strip())                         # total piece splits at "=" and stores the number after it and converted to integer

    return {"server" : hostname , "used" : used , "total" : total}     # return the data into a cleaned dictionary

def status_of(record): 
    """Return Over LImit, Warning and Ok based on the percent used"""
    percent = (record["used"] / record["total"]) * 100                 # to calculate the percentage of the total used 
    if percent >= 100:
        return "Over Limit"
    elif percent >= 90:
        return "Warning"
    else:
        return "OK"
    
# ====================================================================== INPUT

with open("server_records.txt") as f:                                  # to open file and read every line into a list 
    raw_records =  f.readlines()

# =============================================================== PROCESS + OUTPUT

total_count = 0                                                        # to count every record processed in the list

flagged = 0                                                            # to count every record which is over limit and warning 

for raw_record in raw_records:                                         # to go through each line in the file one at a time
    record = parse_line(raw_record)                                    # to clean line into a dictionary

    status  = status_of(record) 
    print(record ," | " ,  status)                                     # to print the cleaned dictionary with its status

    total_count += 1                                                   # to count each line present

    if status != "OK":                                                 # if the status is not equal to ok then it gets adde to flagged
        flagged += 1

print("=" * 50)
print("Total records: " , total_count , " | " , "Flagged: " , flagged) # to print the summary of total records present and how many are not ok
print("=" * 50)

# ==========================================================================

