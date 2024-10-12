from flask import Flask, jsonify
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)

client = MongoClient(MONGO_URI)
db = client['real_time_data']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(db.data_collection.find().sort('timestamp', -1).limit(100))
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
