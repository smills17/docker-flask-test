from flask import Flask,render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    try:
        current_time = time.strftime('%X %x %Z')
        return render_template('index.html', time=current_time)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8087)
