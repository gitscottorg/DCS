from flask import Flask, render_template
import logging
import os

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

@app.route('/')
def home():
    logging.info('Loading index.html')
    return render_template('index.html')

if __name__ == "__main__":
    port = 5001
    app.run(debug=True, host='0.0.0.0', port=port)
    logging.info('Starting webserver, port=%s', port)