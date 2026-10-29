"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  : IT
Date  : 10/18/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """Return OVER LIMIT, WARNING, OK based on percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value , limit):
    """Reture differnce and percentage between value and limit"""
    difference = limit - value
    percent = (value/limit)*100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    print(f"Used    :   {value:>5.2f}")
    print(f"Total   :   {limit:>5.2f}")
    print(f"Free    :   {difference:>5.2f}")
    print(f"Percent :   {percent:.2f}%")
    print(f"Status  :   {status}")

# ================================================================ STORE
records = [{"label" : "Computer" , "value" : "900" , "limit" : "1000"},
           {"label" : "Laptop" , "value" : "190" , "limit" : "120"},
           {"label" : "Phone" , "value" : "60" , "limit" : "100"},]   

# ================================================================ PROCESS AND OUTPUT
over_limit_count = 0

with open("Records.txt" , "w") as f:
    """Extract data from dictionary"""
    for record in records:
        label_ = record["label"]
        value_ = float(record["value"])
        limit_ = float(record["limit"])

        difference, percent = check(value_, limit_)
        status = status_of(percent)

        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {label_}")
        print("=" * 34)
        print_report(label_, value_, limit_, difference, percent, status)

        if status == "OVER LIMIT":
            over_limit_count += 1
            
        f.write(f"{label_}, {status}\n")
print(f"Number of records that are over limit: {over_limit_count}")
