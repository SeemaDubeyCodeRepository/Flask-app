from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host='db',
            database='quotesdb',
            user='postgres',
            password='secret'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from PostgreSQL!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h2>{result[0]}</h2>"
    except Exception as e:
        return f"<p>Database connection failed: {e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)