# Real-Time Notifications with Flask and WebSockets

This project demonstrates how to implement real-time notifications in a web application using Flask combined with WebSockets (via Flask-SocketIO). Whenever a message is sent in the chat interface, it is instantly broadcast and displayed to all connected users without requiring a page refresh.

## Features

- Real-time message delivery and notification
- Simple chat interface powered by Flask and Socket.IO
- Responsive design with basic CSS

## How it Works

- The frontend connects to the Flask backend using WebSockets for two-way communication.
- When a user submits a message, it is sent to the server, which then emits it to all other connected clients in real time.
- The chat window updates instantly for all users, demonstrating the real-time notification capability.

## Stack

- **Flask**
- **Flask-SocketIO**
- **HTML/CSS/JavaScript** (with Socket.IO client)

## Getting Started

1. Install dependencies:
    ```
    pip install requirements.txt
    ```

2. Run the Flask application:
    ```
    python app.py
    ```

3. Open your browser and view your local server to test real-time notifications.

