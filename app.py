from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='lamnguyen',
        password='password',
        database='keyword_search_volume_db'
    )


def format_datetime(dt):
    return dt.strftime('%Y/%m/%d %H:%M:%S')

@app.route('/query', methods=['POST'])
def query_data():
    data = request.json
    user_id = data['user_id']
    keywords = data['list_keywords']
    timing = data['timing']
    start_time = data['start_time']
    end_time = data['end_time']

    conn = get_db_connection()
    cursor = conn.cursor()

    keyword_ids = ', '.join(map(str, keywords))
   
    query_daily = """
        SELECT ksv.keyword_id, DATE(ksv.created_datetime) as date, SUM(ksv.search_volume) as search_volume
        FROM keyword_search_volume ksv
        JOIN user_subscription us ON ksv.keyword_id = us.keyword_id
        WHERE us.user_id = %s
        AND us.subscription_type = 'daily'
        AND ksv.created_datetime BETWEEN '%s' AND '%s'
        AND ksv.keyword_id IN (%s)
        GROUP BY ksv.keyword_id, DATE(ksv.created_datetime)
    """ % (user_id, start_time, end_time, keyword_ids)

    cursor.execute(query_daily)
    daily_data = cursor.fetchall()
             
    if timing == 'daily':

        result = [
            {
                "keyword_id": row[0],
                "datetime": row[1].strftime('%Y/%m/%d %H:%M:%S'),
                "search_volume": row[2],
                "timing": 'daily'
            } for row in daily_data
        ]

    else:
        query_hourly = """
            SELECT ksv.keyword_id, ksv.created_datetime, ksv.search_volume
            FROM keyword_search_volume ksv
            JOIN user_subscription us ON ksv.keyword_id = us.keyword_id
            WHERE us.user_id = %s
            AND us.subscription_type = 'hourly'
            AND ksv.created_datetime BETWEEN '%s' AND '%s'
            AND ksv.keyword_id IN (%s)
        """ % (user_id, start_time, end_time, keyword_ids)

        cursor.execute(query_hourly)
        hourly_data = cursor.fetchall()

        hourly_data = [
            {
                "keyword_id": row[0],
                "datetime": row[1].strftime('%Y/%m/%d %H:%M:%S'),
                "search_volume": row[2],
                "timing": 'hourly'
            } for row in hourly_data
        ]
        daily_data = [
            {
                "keyword_id": row[0],
                "datetime": row[1].strftime('%Y/%m/%d %H:%M:%S'),
                "search_volume": row[2],
                "timing": 'daily'
            } for row in daily_data
        ]
        result = list(hourly_data) + list(daily_data)

    cursor.close()
    conn.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=4000, debug=True)
