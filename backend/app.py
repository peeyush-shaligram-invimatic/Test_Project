import time
import redis
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

# Redis setup
cache = redis.Redis(host='redis', port=6379)

# PostgreSQL setup
conn = psycopg2.connect(
    host='db',
    database='postgres',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS visits (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Swagger setup
SWAGGER_URL = '/docs'
API_URL = '/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Visit Counter API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.yaml')
def swagger_spec():
    return app.send_static_file('swagger.yaml')

# Hit counter logic
def get_hit_count():
    retries = 5
    while True:
        try:
            cur.execute("INSERT INTO visits DEFAULT VALUES")
            conn.commit()
            return cache.incr('hits')
        except (redis.exceptions.ConnectionError, psycopg2.Error) as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# API route for Swagger
@app.route('/api/hit')
def api_hit():
    count = get_hit_count()
    return jsonify(message=f"You've hit the API {count} times.")

# Default route for browser
@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'
