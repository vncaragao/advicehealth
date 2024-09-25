from app import app

@app.route('/')
def home():
    return 'Healthy'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)