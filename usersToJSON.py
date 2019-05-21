import json
import csv

cols = (("first_name", "string", True),
        ("last_name", "string", True),
        ("company_name", "string", True),
        ("address", "string", True),
        ("city", "string", True),
        ("county", "string", True),
        ("state", "string", True),
        ("zip", "string", True),
        ("phone1", "string", True),
        ("phone2", "string", True),
        ("email", "string", True),
        ("web", "string", True))

def main():
    with open("us-50000.csv", "rt", encoding="UTF-8") as f:
        csvreader = csv.reader(f, delimiter=',')
        next(csvreader, None)
        for row in csvreader:
            record = {}
            for i in range(len(cols)):
                name, type, include = cols[i]
                if row[i] != "" and include:
                    if type in ("int", "long"):
                        record[name] = int(row[i])
                    elif type == "double":
                        record[name] = float(row[i])
                    elif type == "string":
                        record[name] = row[i]
            print(json.dumps(record, ensure_ascii=False))

if __name__ == "__main__":
    main()