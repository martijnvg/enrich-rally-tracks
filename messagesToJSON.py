import json
import csv
import random
from datetime import datetime
import string
import time

def random_date():
    d = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(d).strftime('%Y-%m-%dT%H:%M:%S')

def main():
    counter = 0
    while counter < 250000:
        with open("us-50000.csv", "rt", encoding="UTF-8") as f:
            csvreader = csv.reader(f, delimiter=',')
            next(csvreader, None)
            for row in csvreader:
                record = {}
                record['email'] = row[10]
                record['message'] = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
                record['received_at'] = random_date()
                print(json.dumps(record, ensure_ascii=False))
                counter += 1
            
if __name__ == "__main__":
    main()