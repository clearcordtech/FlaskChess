from flask_app import app

app = application

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
