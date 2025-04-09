# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/ping')
# def ping():
#     return jsonify({"status": "ok"})
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int("5000"), debug=True)


from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    count = redis_client.incr('visits')
    return jsonify({"visits": count})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')