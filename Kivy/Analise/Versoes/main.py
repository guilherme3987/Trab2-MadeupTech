import matplotlib.pyplot as plt
from datetime import datetime

# Data (tags and dates)
data = [
    ("2.3.0", "2024-01-05 10:40:12"),
    ("2.3.0rc3", "2024-01-01 12:06:40"),
    ("2.3.0rc2", "2023-12-29 10:12:47"),
    ("2.3.0rc1", "2023-12-28 13:54:57"),
    ("2.3.0dev0", "2023-12-27 11:22:08"),
    ("2.2.1", "2023-06-17 17:09:34"),
    ("2.2.0", "2023-05-20 09:46:34"),
    ("2.2.0rc1", "2023-05-04 07:13:57"),
    ("2.2.0dev0", "2023-04-23 09:53:04"),
    ("2.1.0", "2022-03-06 09:10:08"),
    ("2.1.0rc3", "2022-03-01 22:59:45"),
    ("2.1.0rc2", "2022-03-01 19:34:02"),
    ("2.1.0rc1", "2022-02-12 23:49:14"),
    ("2.1.0dev0", "2022-01-31 18:26:10"),
    ("2.0.0", "2020-12-09 16:22:09"),
    ("2.0.0rc4", "2020-10-15 03:27:46"),
    ("2.0.0rc3", "2020-06-14 22:37:31"),
    ("2.0.0rc2", "2020-04-29 00:55:41"),
    ("2.0.0rc1", "2019-12-29 14:49:55"),
    ("1.11.1", "2019-06-20 13:49:12"),
    ("1.11.0", "2019-06-01 11:48:17"),
    ("1.11.0rc2", "2019-05-29 17:43:31"),
    ("1.11.0rc1", "2019-05-16 09:32:00"),
    ("1.10.1", "2018-06-17 16:46:45"),
    ("1.10.0", "2017-05-07 18:51:32"),
]

# Converting dates to datetime objects
dates = [datetime.strptime(d[1], '%Y-%m-%d %H:%M:%S') for d in data]
tags = [d[0] for d in data]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates, tags, marker='o', linestyle='-', color='b')

# Format the plot
plt.title('Versões entre os anos')
plt.xlabel('Data')
plt.ylabel('Versões')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()