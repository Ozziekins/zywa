from flask import Flask, request, jsonify, render_template
import psycopg2
import psycopg2.extras
from db_config import DATABASE_PARAMS 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_card_status', methods=['POST'])
def get_card_status():
    data = request.get_json()
    card_id = data.get('card_id')
    user_mobile = data.get('user_mobile')
    
    # make sure at least one of card_id or user_mobile is provided
    if not card_id and not user_mobile:
        return jsonify({"error": "Please provide either card_id or user_mobile"}), 400

    query = ""
    query_params = ()

    # make the query
    if card_id:
        query = "SELECT card_id, user_mobile, status, timestamp FROM card_status_table WHERE card_id = %s ORDER BY timestamp DESC LIMIT 1"
        query_params = (card_id,)
    elif user_mobile:
        query = "SELECT card_id, user_mobile, status, timestamp FROM card_status_table WHERE user_mobile = %s ORDER BY timestamp DESC LIMIT 1"
        query_params = (user_mobile,)

    # connect to the database and execute the query
    try:
        conn = psycopg2.connect(**DATABASE_PARAMS)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query, query_params)
        card_info = cursor.fetchone()

        if not card_info:
            return jsonify({"error": "Card not found"}), 404
        
        response_data = {
            "card_id": card_info['card_id'],
            "user_mobile": card_info['user_mobile'],
            "status": card_info['status'],
            "timestamp": card_info['timestamp'].strftime("%Y-%m-%d %H:%M:%S") 
        }
        return jsonify(response_data), 200
    
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500
    
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
