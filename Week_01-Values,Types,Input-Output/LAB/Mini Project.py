server_name = input("Enter server name : ")
used = float(input("Enter used space : "))
total = float(input("Enter total space : "))

free = total - used
percent_used = (used / total) * 100

print("=" * 60)
print(f"Record Check - {server_name}")   
print("=" * 60)
print(f"Used : {used:>10.2f} GB")
print(f"Total : {total:>10.2f} GB")
print(f"Free : {free:>10.2f} GB")
print(f"Percentage Used : {percent_used:>10.2f} %")
print("=" * 60)
