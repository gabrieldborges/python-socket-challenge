from flask import Flask , render_template
from flask_socketio import SocketIO , emit


app = Flask(__name__)

socketio = SocketIO(app)



@app.route('/' , methods = ['GET'])
def index():
    return render_template('index.html')



@socketio.on('message')
def detect_message(msg):
    print("Message detected")
    socketio.emit('message', msg)



if __name__ == "__main__":
    socketio.run(app , debug=True)

