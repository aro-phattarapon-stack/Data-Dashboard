import random
from datetime import datetime

now = datetime.now()
methods = ["GET", "POST", "DELETE"]
endpoints = ["/home", "/products", "/login", "/dashboard", "/contact"]
endpoint_weights = [50, 25, 10, 10, 5]
HTTPstatus = ["200", "404", "400", "500"]
status_weights = [85, 10, 3, 2]

with open("access.log", "w", encoding="utf-8") as f:
    for log in range(2000):
        ip = random.randint(1, 255)
        method = random.choice(methods)
        endpoint = random.choices(endpoints, weights=endpoint_weights)[0]
        status = random.choices(HTTPstatus, weights=status_weights)[0]
        size = random.randint(200, 5000)
        timestamp = now.strftime("%d/%b/%Y:%H:%M:%S")

        log_line = f"192.168.1.{ip} - - [{timestamp}] \"{method} {endpoint} HTTP/1.1\" {status} {size}\n"
        f.write(log_line)
        pass

print("สร้างไฟล์ access.log เสร็จเรียบร้อย")
