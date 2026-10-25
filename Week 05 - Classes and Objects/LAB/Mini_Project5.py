"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  : IT
Date  : 12/23/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def percent(self):
        percentage = (self.value/self.limit) * 100
        return percentage
    
    def status(self):
        """Return the status after calculating the percentage"""
        p = self.percent()
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
def load_records(path):
    records = []
    with open (path)as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
result = load_records("Records.txt")

# ==================================================================== OUTPUT
for record in result:
    print()
    print("=" * 34)
    print(f"     RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Label:             {record.label}")
    print(f"Value:             {record.value}")
    print(f"Limit:             {record.limit}")
    print(f"Status:            {record.status()}")
    print("=" * 34)
    print(f"Total records that are OVER LIMIT: {Record.over_limit_count}")
    print("=" * 34)
    print("=" * 34)
