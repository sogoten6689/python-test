import random
from datetime import datetime, timedelta
import mysql.connector


# # Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='lamnguyen',
    password='password',
    database='keyword_search_volume_db'
)
cursor = conn.cursor()

# Insert 10 keywords
keywords = ['shoes', 'T-shirt', 'Iphone', 'laptop', 'headphones', 'watch', 'backpack', 'sunglasses', 'camera', 'tablet']
for keyword in keywords:
    cursor.execute("INSERT INTO keyword (keyword_name) VALUES (%s)", (keyword,))
conn.commit()

# Generate search volume data for 3 months
end_date = datetime.now()
start_date = end_date - timedelta(days=90)
keywords_ids = list(range(1, 11))

for keyword_id in keywords_ids:
    current_date = start_date
    while current_date <= end_date:
        search_volume = random.randint(100, 1000)
        cursor.execute(
            "INSERT INTO keyword_search_volume (keyword_id, created_datetime, search_volume) VALUES (%s, %s, %s)",
            (keyword_id, current_date, search_volume)
        )
        current_date += timedelta(hours=1)
    conn.commit()
cursor.close()
conn.close()
